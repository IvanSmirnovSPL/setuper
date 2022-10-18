from pathlib import Path
import os
import glob
import subprocess
import shutil
import threading

# 0.orig
from libs.fill.p_rgh import fill_p_rgh
from libs.fill.alpha_water import fill_alpha_water
from libs.fill.U import fill_U


def makeFilesInZeroDir(self):
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