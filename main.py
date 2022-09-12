from pathlib import Path
import os
import glob
import subprocess
import shutil

# constant
from libs.fill.g import fill_g
from libs.fill.transportProperties import fill_transportProperties
from libs.fill.turbulenceProperties import fill_turbulenceProperties

# 0.orig
from libs.fill.p_rgh import fill_p_rgh
from libs.fill.alpha_water import fill_alpha_water
from libs.fill.U import fill_U

# system
from libs.fill.controlDict import fill_controlDict
from libs.fill.decomposeParDict import fill_decomposeParDict
from libs.fill.fvSchemes import fill_fvSchemes
from libs.fill.fvSolution import fill_fvSolution

# support
from libs.file_design import FileDesign
from libs import params
from libs.parseArgs import fillFromUserDict, userFlags, dictFromUserFlags

files_data = params.files_data


class PathsOfCase:
    def __init__(self, name='new_case', files_data={}, output_path="", grid_path=""):
        self.fd = FileDesign()
        self.files_data = files_data
        self.home_directory = Path.cwd()
        self.case_directory = Path(self.home_directory, name)
        self.constant_dir_path = Path(self.case_directory, 'constant')
        self.zero_dir_path = Path(self.case_directory, '0.orig')
        self.system_dir_path = Path(self.case_directory, 'system')
        self.output_path = output_path
        self.reConstract = False
        if grid_path == "":
            self.grid_path = Path(self.constant_dir_path, "polyMesh")
        else:
            self.grid_path = grid_path  # path to /polymesh
        if output_path == "":
            self.output_path = Path(self.case_directory, "output.txt")
        else:
            self.output_path = output_path

    def start_case(self):
        # if not os.path.exists(Path(self.constant_dir_path, "polyMesh")):
        #     list_files = subprocess.run(["ln", "-s", self.grid_path, Path(self.constant_dir_path, "polyMesh")])
        # list_files = subprocess.run(["cp", "-r", self.zero_dir_path, Path(self.case_directory, "0")])

        if os.path.exists(Path(self.constant_dir_path, "polyMesh")):
            os.remove(Path(self.constant_dir_path, "polyMesh"))
        os.symlink(self.grid_path, Path(self.constant_dir_path, "polyMesh"))

        if os.path.exists(Path(self.case_directory, "0")):
            os.remove(Path(self.case_directory, "0"))
        shutil.copytree(self.zero_dir_path, Path(self.case_directory, "0"))


        (open(self.output_path, 'w')).close()  # clear output file
        np = int(self.files_data['system']['decomposeParDict']['numberOfSubdomains'])
        if np == 1:
            os.system('interPhaseChangeFoam -case {case} >> {output}'.format(case=self.case_directory,
                                                                             output=self.output_path))
        else:
            self.reConstract = True
            os.system('decomposePar -case {case} >> {output}'.format(
                case=self.case_directory,
                output=self.output_path, np=np))
            os.system('mpirun -np {np} interPhaseChangeFoam -case {case} -parallel  >> {output}'.format(
                case=self.case_directory,
                output=self.output_path, np=np))
        #if self.reConstract:
        #    os.system('reconstractPar')

    def make_directories(self):
        self.existence_check_and_make(self.case_directory)
        self.existence_check_and_make(self.constant_dir_path)
        self.existence_check_and_make(self.zero_dir_path)
        self.existence_check_and_make(self.system_dir_path)

    def make_files_in_constant_dir(self):
        files = list(self.files_data['constant'].keys())  # g, transportProperties, turbulenceProperties
        data = self.files_data['constant']
        functions = {'g': fill_g, 'transportProperties': fill_transportProperties,
                     'turbulenceProperties': fill_turbulenceProperties}
        for file_ in files:
            path = Path(self.constant_dir_path, file_)
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file_)
            out_stream = open(path, 'a')
            param = data[file_]
            out_stream.write(functions[file_](param))
            out_stream.close()

    def make_files_in_system_dir(self):
        files = list(self.files_data['system'].keys())  # controlDict,
        # decomposeParDict, fvSchemes, fvSolution
        files.remove('blockMeshDict')
        files.remove('snappyHexMeshDict')
        data = self.files_data['system']
        functions = {'controlDict': fill_controlDict,
                     'decomposeParDict': fill_decomposeParDict, 'fvSchemes': fill_fvSchemes,
                     'fvSolution': fill_fvSolution}
        for file_ in files:
            path = Path(self.system_dir_path, file_)
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file_)
            out_stream = open(path, 'a')
            param = data[file_]
            out_stream.write(functions[file_](param))
            out_stream.close()

    def make_files_in_zero_dir(self):
        files = list(self.files_data['0.orig'].keys())  # p_rgh, U, alpha.water
        data = self.files_data['0.orig']
        functions = {'p_rgh': fill_p_rgh, 'U': fill_U, 'alpha.water': fill_alpha_water}
        field = ['volScalarField', 'volVectorField']
        classes = {'p_rgh': field[0], 'U': field[1], 'alpha.water': field[0]}

        for file_ in files:
            path = Path(self.zero_dir_path, file_)
            self.fd.init_file(path)
            self.fd.foamfile(path=path, class_=classes[file_], object_=file_)
            out_stream = open(path, 'a')
            params = data[file_]
            functions[file_](params, fp=out_stream)
            out_stream.close()

    @staticmethod
    def existence_check_and_make(path):
        if not os.path.exists(path):
            os.mkdir(path)


def clear_case(path):
    names = os.listdir(path)
    for name in names:
        fullname = os.path.join(path, name)
        if name != 'system' and name != 'constant' and name != '0.orig':
            if os.path.isfile(fullname):
                os.remove(fullname)
            else:
                shutil.rmtree(fullname, ignore_errors=True)


def main():
    userDict = {}
    for filename in glob.glob('*param*'):
        with open(Path(Path.cwd(), filename), 'r') as f:
            for line in f:
                key, data = line.split(':', 1)
                userDict[key] = data
        break

    fillFromUserDict(userDict, files_data)
    parser = userFlags()
    args = parser.parse_args()
    userDict = dictFromUserFlags(args)
    fillFromUserDict(userDict, files_data)

    if args.clear_case_path is not None:
        try:
            clear_case(args.clear_case_path)
        except Exception:
            print('The case in {} does not exist'.format(args.clear_case_path))
    elif args.reconstruct_case_path is not None:
        os.system('reconstructPar -case {}'.format(args.reconstruct_case_path))
    else:

        paths = PathsOfCase(name=args.name_case, files_data=files_data, grid_path=args.grid_path,
                            output_path=args.output_path)
        paths.make_directories()
        paths.make_files_in_system_dir()
        paths.make_files_in_constant_dir()
        paths.make_files_in_zero_dir()
        paths.start_case()


if __name__ == '__main__':
    main()
