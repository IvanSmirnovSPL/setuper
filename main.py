from pathlib import Path
import os
import argparse


from libs.fill.transportProperties import fill_transportProperties
from libs.fill.blockMeshDict import fill_blockMeshDict
from libs.fill.controlDict import fill_cohntrolDict
from libs.fill.decomposeParDict import fill_decomposeParDict
from libs.fill.fvSchemes import fill_fvSchemes
from libs.fill.fvSolution import fill_fvSolution
from libs.fill.PDRblockMeshDcit import fill_PDRblockMeshDict
from libs.fill.p import fill_p
from libs.fill.U import fill_U
from libs.file_design import FileDesign
from libs import params

files_data = params.files_data

class PathsOfCase:
    def __init__(self, name='new_case', files_data={}):
        self.fd = FileDesign()
        self.files_data = files_data
        self.home_directory = Path.cwd()
        self.case_directory = Path(self.home_directory, name)
        self.constant_dir_path = Path(self.case_directory, 'constant')
        self.zero_dir_path = Path(self.case_directory, '0')
        self.system_dir_path = Path(self.case_directory, 'system')

    def make_directories(self):
        self.existence_check_and_make(self.case_directory)
        self.existence_check_and_make(self.constant_dir_path)
        self.existence_check_and_make(self.zero_dir_path)
        self.existence_check_and_make(self.system_dir_path)

    def make_files_in_system_dir(self):
        files = list(self.files_data['system'].keys())
        data = self.files_data['system']
        for file in files:
            path = Path(self.system_dir_path, file)
            inf = data[file]
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file)
        fill_blockMeshDict(self.fd, Path(self.system_dir_path, files[0]),
                           data[files[0]])
        fill_cohntrolDict(self.fd, Path(self.system_dir_path, files[1]),
                           data[files[1]])
        fill_decomposeParDict(self.fd, Path(self.system_dir_path, files[2]),
                          data[files[2]])
        fill_fvSchemes(self.fd, Path(self.system_dir_path, files[3]),
                              data[files[3]])
        fill_fvSolution(self.fd, Path(self.system_dir_path, files[4]),
                       data[files[4]])
        fill_PDRblockMeshDict(self.fd, Path(self.system_dir_path, files[5]),
                        data[files[5]])

    def make_files_in_constant_dir(self):
        files = list(self.files_data['constant'].keys())
        data = self.files_data['constant']
        for file in files:
            path = Path(self.constant_dir_path, file)
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file)

        fill_transportProperties(self.fd, Path(self.constant_dir_path, files[0]),
                                 data[files[0]])

    def make_files_in_zero_dir(self):
        field = ['volScalarField', 'volVectorField']
        files = list(self.files_data['0'].keys())
        data = self.files_data['0']

        path = Path(self.zero_dir_path, files[0])
        inf = data[files[0]]
        self.fd.init_file(path)
        self.fd.foamfile(path=path, class_=field[0], object_=files[0])
        fill_p(self.fd, Path(self.zero_dir_path, files[0]),
                            data[files[0]])

        path = Path(self.zero_dir_path, files[1])
        inf = data[files[1]]
        self.fd.init_file(path)
        self.fd.foamfile(path=path, class_=field[1], object_=files[1])
        fill_U(self.fd, Path(self.zero_dir_path, files[1]),
               data[files[1]])

    @staticmethod
    def existence_check_and_make(path):
        if not os.path.exists(path):
            os.mkdir(path)


def main():

    parser = argparse.ArgumentParser(description="A program for generating files for cavity case")
    parser.add_argument('-n', '--name_case', metavar='', type=str, default='new_case', help="A path to place results.")
    args = parser.parse_args()

    paths = PathsOfCase(name=args.name_case, files_data=files_data)
    paths.make_directories()
    paths.make_files_in_system_dir()
    paths.make_files_in_constant_dir()
    paths.make_files_in_zero_dir()


if __name__ == '__main__':
    main()
