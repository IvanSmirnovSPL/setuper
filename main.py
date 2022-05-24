from pathlib import Path
import os

from libs.fill.transportProperties import fill_transportProperties
from libs.file_design import FileDesign

files_data = {
    'system':
        {
            'blockMeshDict': 0, 'controlDict': 0, 'decomposeParDict': 0,
            'fvSchemes': 0, 'fvSolution': 0, 'PDRblockMeshDict': 0
        },
    'constant':
        {'transportProperties': {'nu': 0.01, 'mu': 0}},
    '0':
        {'p': 0, 'U': 0}
}


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
        files = self.files_data['system'].keys()
        data = self.files_data['system']
        for file in files:
            path = Path(self.system_dir_path, file)
            inf = data[file]
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file)

    def make_files_in_constant_dir(self):
        files = self.files_data['constant'].keys()
        data = self.files_data['constant']
        for file in files:
            path = Path(self.constant_dir_path, file)
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file)
            fill_transportProperties(self.fd, path, data[file])

    def make_files_in_zero_dir(self):
        files = self.files_data['0'].keys()
        data = self.files_data['0']
        for file in files:
            path = Path(self.zero_dir_path, file)
            inf = data[file]
            self.fd.init_file(path)
            self.fd.foamfile(path=path, object_=file)



    def fill_blockMeshDict(self, scale=1):
        file = open(Path(self.system_dir_path, 'blockMeshDict'), 'a')

        file.write(self.fd.line())
        file.write(self.fd.string_with_spaces('scale', start_space=0))
        file.write(self.fd.line(str(scale) + ';'))

        file.write(self.fd.line())
        file.write(self.fd.line('vertices'))
        file.write(self.fd.line('('))
        file.write('(0 0 0)' + '\n' + '(0.1 0 0)' + '\n' + '(0.1 0.1 0)' + '\n' +
                   '(0 0.1 0)' + '\n' + '(0 0 0.01)' + '\n' + '(0.1 0 0.01)' + '\n' +
                   '(0.1 0.1 0.01)' + '\n' + '(0 0.1 0.01)' + '\n')
        file.write(self.fd.line(');'))

        file.write(self.fd.separator)
        file.close()


    @staticmethod
    def existence_check_and_make(path):
        if not os.path.exists(path):
            os.mkdir(path)


def main():
    paths = PathsOfCase(files_data=files_data)
    paths.make_directories()
    paths.make_files_in_system_dir()
    paths.make_files_in_constant_dir()
    paths.make_files_in_zero_dir()


if __name__ == '__main__':
    main()
