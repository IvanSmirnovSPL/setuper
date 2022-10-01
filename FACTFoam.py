from pathlib import Path
import os
import glob
import subprocess
import shutil

# constant
from libs.fill.g import fill_g
from libs.fill.thermophysicalProperties import fill_thermophysicalProperties
from libs.fill.turbulenceProperties import fill_turbulenceProperties

# 0.orig
from libs.fill.p import fill_p
from libs.fill.alpha_water import fill_alpha_water
from libs.fill.U import fill_U
from libs.fill.T import fill_T

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
    def __init__(self, name='new_case', vtk='new_case_', files_data={}, output_path="", grid_path="", table_path=""):
        self.fd = FileDesign()
        self.files_data = files_data
        self.home_directory = Path.cwd()
        self.case_directory = Path(self.home_directory, name)
        self.vtk_directory = Path(self.home_directory, vtk)
        self.constant_dir_path = Path(self.case_directory, 'constant')
        self.zero_dir_path = Path(self.case_directory, '0.orig')
        self.system_dir_path = Path(self.case_directory, 'system')
        self.output_path = output_path
        self.reConstract = False
        if grid_path == "":
            self.grid_path = Path(self.constant_dir_path, "polyMesh")
        else:
            self.grid_path = grid_path  # path to /polymesh
        if table_path == "":
            self.table = Path(self.constant_dir_path, "tables")
        else:
            self.table_path = table_path  # path to /polymesh
        if output_path == "":
            self.output_path = Path(self.case_directory, "output.txt")
        else:
            self.output_path = Path(self.case_directory, "output.txt")

    def add_paths(self):
        self.grid_path = self.find('polyMesh', Path.cwd())
        self.table_path = self.find('tables', Path.cwd())

        if os.path.exists(Path(self.constant_dir_path, "polyMesh")):
            os.remove(Path(self.constant_dir_path, "polyMesh"))
        os.symlink(self.grid_path, Path(self.constant_dir_path, "polyMesh"))

        if os.path.exists(Path(self.constant_dir_path, "tables")):
            os.remove(Path(self.constant_dir_path, "tables"))
        os.symlink(self.table_path, Path(self.constant_dir_path, "tables"))

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in dirs:
                return str(os.path.join(root, name))

    def start_case(self):

        if os.path.exists(Path(self.case_directory, "0")):
            os.remove(Path(self.case_directory, "0"))
        shutil.copytree(self.zero_dir_path, Path(self.case_directory, "0"))

        (open(self.output_path, 'w')).close()  # clear output file
        #np = int(self.files_data['system']['decomposeParDict']['numberOfSubdomains'])
        np = 1
        os.system('source /opt/kpvm/foam2112rc')
        os.system('source /opt/kpvm/ifrolov/bin/bubblerc')
        if np == 1:
            os.system('FAKTFoam -case {case} >> {output}'.format(case=self.case_directory,
                                                                             output=self.output_path))
        else:
            self.reConstract = True
            os.system('decomposePar -case {case} >> {output}'.format(
                case=self.case_directory,
                output=self.output_path, np=np))
            os.system('mpirun -np {np} FAKTFoam -case {case} -parallel  >> {output}'.format(
                case=self.case_directory,
                output=self.output_path, np=np))

            os.system('reconstructPar -case {case} >> {output}'.format(case=self.case_directory,
                                                                       output=self.output_path))

        os.system(f'foamToVTK -case {self.case_directory} >> {self.output_path}')
        shutil.copytree(Path(self.case_directory, 'VTK'), Path(self.vtk_directory, 'VTK'))

    def make_directories(self):
        self.existence_check_and_make(self.case_directory)
        self.existence_check_and_make(self.constant_dir_path)
        self.existence_check_and_make(self.zero_dir_path)
        self.existence_check_and_make(self.system_dir_path)

    def make_files_in_constant_dir(self):
        files = list(self.files_data['constant'].keys())  # g, transportProperties, turbulenceProperties
        # files.remove('transportProperties')
        data = self.files_data['constant']
        functions = {'g': fill_g, 'thermophysicalProperties': fill_thermophysicalProperties,
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
        # files.remove('blockMeshDict')
        # files.remove('snappyHexMeshDict')
        # files.remove('decomposeParDict')
        data = self.files_data['system']
        functions = {'controlDict': fill_controlDict,
                     'fvSchemes': fill_fvSchemes,
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
        functions = {'p': fill_p, 'U': fill_U, 'alpha.water': fill_alpha_water, 'T': fill_T}
        field = ['volScalarField', 'volVectorField']
        classes = {'p': field[0], 'U': field[1], 'alpha.water': field[0], 'T': field[0]}

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

        paths = PathsOfCase(name=args.name_case, vtk=args.vtk_path, files_data=files_data, grid_path=args.grid_path,
                            table_path=args.table_path,
                            output_path=args.output_path)
        paths.make_directories()
        paths.make_files_in_system_dir()
        paths.make_files_in_constant_dir()
        paths.make_files_in_zero_dir()
        paths.add_paths()
        paths.start_case()


if __name__ == '__main__':
    main()
