from pathlib import Path

# 0.orig
from libs.fill.p import fill_p
from libs.fill.alpha_water import fill_alpha_water
from libs.fill.U import fill_U
from libs.fill.T import fill_T
from libs.makeZeroFromMesh import detectBTypes
from libs.fill.writeZeroHardCode import writeAlpha, writeP, writeT, writeU, writeInfConditions

# support
from libs.fields import refactorTypes


def makeFilesInZeroDir(self):
    files = ['T', 'p', 'U', 'alpha.vapour']
    functions = {'T': writeT(), 'p': writeP(), 'U': writeU(), 'alpha.vapour': writeAlpha()}

    for file_ in files:
        path = Path(self.zero_dir_path, file_)
        out_stream = open(path, 'w')
        print(functions[file_], file=out_stream)
        out_stream.close()
    data = self.files_data['0.orig']['infConditions']
    path = Path(self.zero_dir_path, 'infConditions')
    out_stream = open(path, 'w')
    print(writeInfConditions(data), file=out_stream)
    out_stream.close()

    # if self.zero_dir_flag is not None:
    #     path = self.find('0', Path.cwd())
    #     print(path)
    #     self.copyDirectories(path, self.zero_dir_path)
    # else:
    #     files = list(self.files_data['0.orig'].keys())  # p_rgh, U, alpha.vapour
    #     data = self.files_data['0.orig']
    #     functions = {'p': fill_p, 'U': fill_U, 'alpha.vapour': fill_alpha_water, 'T': fill_T}
    #     field = ['volScalarField', 'volVectorField']
    #     classes = {'p': field[0], 'U': field[1], 'alpha.vapour': field[0], 'T': field[0]}
    #     types = refactorTypes(detectBTypes(self.grid_path))
    #
    #     for f in functions.keys():
    #         self.files_data['0.orig'][f]['boundary_types'] = types
    #
    #     for file_ in files:
    #         path = Path(self.zero_dir_path, file_)
    #         self.fd.init_file(path)
    #         self.fd.foamfile(path=path, class_=classes[file_], object_=file_)
    #         out_stream = open(path, 'a')
    #         params = data[file_]
    #         functions[file_](params, fp=out_stream, p=r'#include "../system/params"')
    #         out_stream.close()
