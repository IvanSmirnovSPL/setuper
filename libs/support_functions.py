import os
import shutil
from pathlib import Path
import glob
from libs.parseArgs import fillFromUserDict, userFlags, dictFromUserFlags


def ExistenceCheckAndMake(path):
    if not os.path.exists(path):
        os.mkdir(path)


def ClearCase(path):
    names = os.listdir(path)
    for name in names:
        fullname = os.path.join(path, name)
        if name != 'system' and name != 'constant' and name != '0.orig':
            if os.path.isfile(fullname):
                os.remove(fullname)
            else:
                shutil.rmtree(fullname, ignore_errors=True)


def Preparation(files_data):
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
            ClearCase(args.clear_case_path)
        except Exception:
            print('The case in {} does not exist'.format(args.clear_case_path))
    elif args.reconstruct_case_path is not None:
        os.system('reconstructPar -case {}'.format(args.reconstruct_case_path))
    else:
        zero_dir_flag = None
        if args.zero_path != 'None':
            zero_dir_flag = args.zero_path
    return args, zero_dir_flag


def AddPaths(self):
    self.grid_path = self.find('polyMesh', Path.cwd())
    if os.path.exists(Path(self.constant_dir_path, "polyMesh")):
        os.remove(Path(self.constant_dir_path, "polyMesh"))
    os.symlink(self.grid_path, Path(self.constant_dir_path, "polyMesh"))

    os.symlink(self.table_path, Path(self.constant_dir_path, "tables"))


def Find(self, name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return str(os.path.join(root, name))
