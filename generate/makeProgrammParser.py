from copy import copy

def makeProgrammSettingsFunction(d, rezPath):
    with open(rezPath, 'w') as f:
        print('def programmSettings(parser):', file=f)
        keys = {}
        keys = unpackDictionary(d, keys)
        for item in keys.items():
            key = item[0]
            default = item[1]

            if isinstance(default, float):
                type_ = 'float'
            elif isinstance(default, int):
                type_ = 'int'
            else:
                type_ = 'str'
                default = r"'" + str(default) + r"'"
            default = str(default)
            print(
                '\t' + r"parser.add_argument('-" + key + r"', '--" + key + r"', metavar='', type=" + type_ + ", default=" + default + r", help='')",
                file=f)


def makeDictFromUserFlags(d, rezPath):
    keys = {}
    keys = unpackDictionary(d, keys)
    with open(rezPath, 'w') as f:
        print('def dictFromUserFlags(args):', file=f)
        print('\t' + 'userDict = {}', file=f)
        for item in keys.items():
            key = item[0]
            default = item[1]
            if str(default).find(' ') != -1:
                print('\t' + r"userDict['" + key + r"'] = '(' + unpackArg(args." + key + r") + ')'", file=f)
            else:
                print('\t' + r"userDict['" + key + r"'] = args." + key, file=f)

def makeFillFromUserDict(d, rezPath):
    keys = {}
    constructDictPath(d, keys, [])
    with open(rezPath, 'w') as f:
        print('def fillFromUserDict(userDict, files_data):', file=f)
        print('\t' + 'for key in userDict.keys():', file=f)
        flag=False
        for key_ in keys:
            path = keys[key_].path
            key = str(keys[key_].item)
            if flag is False:
                tmp='if'
                flag=True
            else:
                tmp='elif'
            path = r"['" + "']['".join(path) + r"']"
            print('\t' * 2 + tmp +r" key = '" + key_ + r"':", file=f)
            print('\t' * 3 + 'files_data' + path + r" = str(userDict[key])", file=f)

d = {'a': {'b': 2}, 'e': {'c': 3., 'd': '0 0 0'}}


def unpackDictionary(d, rez):
    for key in d.keys():
        if isinstance(d[key], dict):
            unpackDictionary(d[key], rez)
        else:
            rez[key] = d[key]

    return rez

class itemWithPath:
    def __init__(self, item, path):
        self.item = item
        self.path = path

def constructDictPath(d, rez, curPath):
    for key in d.keys():
        if isinstance(d[key], dict):
            cP = []
            if len(curPath) > 0:
                cP = curPath.copy()
            cP.append(key)
            constructDictPath(d[key], rez, cP)
        else:
            #print('here', key, curPath)
            #curPath.append(key)
            rezPath = curPath.copy()
            rezPath.append(key)
            rez[key] = itemWithPath(d[key], rezPath)
    return rez
