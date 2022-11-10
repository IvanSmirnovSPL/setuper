from pathlib import Path

# system
from libs.fill.controlDict import fill_controlDict
from libs.fill.decomposeParDict import fill_decomposeParDict
from libs.fill.fvSchemes import fill_fvSchemes
from libs.fill.fvSolution import fill_fvSolution
#from libs.fill.params_file import fill_params
#from libs.fill.setFieldsDict import fill_SetFieldsDict


def makeFilesInSystemDir(self):
    files = list(self.files_data['system'].keys())  # controlDict,
    # decomposeParDict, fvSchemes, fvSolution
    data = self.files_data['system']
    functions = {'controlDict': fill_controlDict,
                 'fvSchemes': fill_fvSchemes,
                 'fvSolution': fill_fvSolution,
                 'decomposeParDict': fill_decomposeParDict,
                 #'setFieldsDict': fill_SetFieldsDict
                }
    for file_ in files:
        path = Path(self.system_dir_path, file_)
        self.fd.init_file(path)
        self.fd.foamfile(path=path, object_=file_)
        out_stream = open(path, 'a')
        param = data[file_]
        out_stream.write(functions[file_](param))
        out_stream.close()