from pathlib import Path
import os
import glob
import subprocess
import shutil
import threading

# system
from libs.fill.controlDict import fill_controlDict
from libs.fill.decomposeParDict import fill_decomposeParDict
from libs.fill.fvSchemes import fill_fvSchemes
from libs.fill.fvSolution import fill_fvSolution


def makeFilesInSystemDir(self):
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