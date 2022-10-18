from pathlib import Path
import os
import glob
import subprocess
import shutil
import threading

from libs.zero_dir import makeFilesInZeroDir
from libs.system_dir import makeFilesInSystemDir
from libs.constant_dir import makeFilesInConstantDir


# support
from libs.file_design import FileDesign
from libs import params
from libs.parseArgs import fillFromUserDict, userFlags, dictFromUserFlags

files_data = params.files_data


class PathsOfCase:
    def __init__(self, name='new_case', vtk='new_case_', zero_dir_flag=None, files_data={}, output_path="", grid_path=""):
        self.fd = FileDesign()
        self.files_data = files_data
        self.home_directory = Path.cwd()
        self.case_directory = Path(self.home_directory, name)
        self.vtk_directory = Path(self.home_directory, vtk)
        self.constant_dir_path = Path(self.case_directory, 'constant')
        self.zero_dir_path = Path(self.case_directory, '0.orig')
        self.zero_dir_flag = zero_dir_flag
        self.system_dir_path = Path(self.case_directory, 'system')
        self.output_path = Path(self.case_directory, output_path)
        self.reConstract = False
        if grid_path == "":
            self.grid_path = Path(self.constant_dir_path, "polyMesh")
        else:
            self.grid_path = grid_path  # path to /polymesh
        if output_path == "":
            self.output_path = Path(self.case_directory, "output.txt")
        else:
            self.output_path = Path(self.case_directory, "output.txt")

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in dirs:
               return str(os.path.join(root, name))



    def start_case(self):

        if os.path.exists(Path(self.case_directory, "0")):
            os.remove(Path(self.case_directory, "0"))
        shutil.copytree(self.zero_dir_path, Path(self.case_directory, "0"))


        (open(self.output_path, 'w')).close()  # clear output file
        np = int(self.files_data['system']['decomposeParDict']['numberOfSubdomains'])
        if np == 1:
            os.system('interPhaseChangeFoam -case {case} >> {output}'.format(case=self.case_directory,
                                                                             output=self.output_path))
        else:
            os.system('decomposePar -case {case} >> {output}'.format(
                case=self.case_directory,
                output=self.output_path, np=np))
            os.system('mpirun -np {np} interPhaseChangeFoam -case {case} -parallel  >> {output}'.format(
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

    def copyDirectories(self, src, dist, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dist, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    def make_files_in_constant_dir(self):
        makeFilesInConstantDir(self)

    def make_files_in_system_dir(self):
        makeFilesInSystemDir(self)

    def make_files_in_zero_dir(self):
        makeFilesInZeroDir(self)

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
        zero_dir_flag = None
        if args.zero_path != 'None':
            zero_dir_flag = args.zero_path

        paths = PathsOfCase(name=args.name_case, vtk=args.vtk_path, zero_dir_flag=zero_dir_flag, files_data=files_data,
                            grid_path=args.grid_path, output_path=args.output_path)
        paths.make_directories()
        paths.make_files_in_system_dir()
        paths.make_files_in_constant_dir()
        paths.make_files_in_zero_dir()
        paths.start_case()


if __name__ == '__main__':
    main()
