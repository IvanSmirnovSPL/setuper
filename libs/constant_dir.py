from pathlib import Path
import os
import glob
import subprocess
import shutil
import threading

# constant
from libs.fill.g import fill_g
from libs.fill.transportProperties import fill_transportProperties
from libs.fill.turbulenceProperties import fill_turbulenceProperties


def makeFilesInConstantDir(self):
    self.grid_path = self.find('polyMesh', Path.cwd())

    if os.path.exists(Path(self.constant_dir_path, "polyMesh")):
        shutil.rmtree(Path(self.constant_dir_path, "polyMesh"))
    os.mkdir(Path(self.constant_dir_path, 'polyMesh'))
    self.copyDirectories(self.grid_path, Path(self.constant_dir_path, 'polyMesh'))
    #os.symlink(self.grid_path, Path(self.constant_dir_path, "polyMesh"))

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