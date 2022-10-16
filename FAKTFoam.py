from pathlib import Path
import os
import shutil

# support
from libs.file_design import FileDesign
from libs import params
from libs.support_functions import ExistenceCheckAndMake, Preparation, AddPaths, Find

from libs.fill.constant_dir import makeFilesInConstantDir
from libs.fill.system_dir import makeFilesInSystemDir
from libs.fill.zero_dir import makeFilesInZeroDir

files_data = params.files_data


class PathsOfCase:
    def __init__(self, name='new_case', vtk='new_case_', zero_dir_flag=None, files_data={}, output_path="",
                 grid_path="", table_path="/opt/kpvm/ismirnov/bin/tables"):
        self.fd = FileDesign()
        self.files_data = files_data
        self.home_directory = Path.cwd()
        self.case_directory = Path(self.home_directory, name)
        self.vtk_directory = Path(self.home_directory, vtk)
        self.constant_dir_path = Path(self.case_directory, 'constant')
        self.zero_dir_path = Path(self.case_directory, '0.orig')
        self.zero_dir_flag = zero_dir_flag
        self.system_dir_path = Path(self.case_directory, 'system')
        self.output_path = output_path

        if grid_path == "":
            self.grid_path = Path(self.constant_dir_path, "polyMesh")
        else:
            self.grid_path = grid_path  # path to /polymesh
        if table_path == "":
            self.table = Path(self.constant_dir_path, "tables")
        else:
            self.table_path = table_path  # path to /tables
        if output_path == "":
            self.output_path = Path(self.case_directory, "output.txt")
        else:
            self.output_path = Path(self.case_directory, "output.txt")

    def add_paths(self):
        AddPaths(self)

    def find(self, name, path):
        return Find(self, name, path)

    def start_case(self):

        if os.path.exists(Path(self.case_directory, "0")):
            os.remove(Path(self.case_directory, "0"))
        shutil.copytree(self.zero_dir_path, Path(self.case_directory, "0"))
        os.system(f'cd {self.case_directory} && setFields >> {self.output_path}')

        (open(self.output_path, 'w')).close()  # clear output file
        np = int(self.files_data['system']['decomposeParDict']['numberOfSubdomains'])
        if np == 1:
            os.system('cd {case} && FAKTFoam >> {output}'.format(case=self.case_directory,
                                                                 output=self.output_path))
        else:
            os.system('decomposePar -case {case} >> {output}'.format(
                case=self.case_directory,
                output=self.output_path, np=np))
            os.system('cd {case} && mpirun -np {np} FAKTFoam -parallel  >> {output}'.format(
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

    def make_files_in_zero_dir(self):
        makeFilesInZeroDir(self)

    def make_files_in_constant_dir(self):
        makeFilesInConstantDir(self)

    def make_files_in_system_dir(self):
        makeFilesInSystemDir(self)

    @staticmethod
    def existence_check_and_make(path):
        ExistenceCheckAndMake(path)


def preparation(files_data):
    return Preparation(files_data)


def main():
    args, zero_dir_flag = preparation(files_data)
    paths = PathsOfCase(name=args.name_case, vtk=args.vtk_path, zero_dir_flag=zero_dir_flag, files_data=files_data,
                        grid_path=args.grid_path, table_path=args.table_path, output_path=args.output_path)
    paths.make_directories()
    paths.make_files_in_system_dir()
    paths.make_files_in_constant_dir()
    paths.make_files_in_zero_dir()
    paths.add_paths()
    paths.start_case()


if __name__ == '__main__':
    main()
