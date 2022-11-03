import re
import os
import shutil
from pathlib import Path

def filePointer(fd=None, fp=None, flag='r'):
    if fp is not None:
        f = open(fp, flag)
    else:
        f = fd
    return f

def searchParam(line, d, part=None):
    tmp = line.rfind(';')
    if tmp == -1 or len(line.split()) < 2 or line.split()[0] == 'dimensions':
        return r"'" + line + r"'"
    lineList = line[:tmp].split()

    st = line.find('(')
    ed = line.find(')')
    key = lineList[0]
    pattern = re.compile('\$.*')
    if pattern.match(key) is not None:
        print(key)
        key = key[1:]
    if part is not None:
        key = part['key'] +f'_{key}'
    for i in range(20):
        key = key.replace('.', '')
        key = key.replace('(', '_')
        key = key.replace(')', '_')
        key = key.replace(',', '_')
        key = key.replace('*', '_')
        key = key.replace('__', '_')
    if st != -1 and ed != -1:
        default = line[st + 1: ed]
        line = line[:st] + '({});' + r"'.format(params['" + key + r"'])"
    else:
        default = lineList[-1]
        line = " ".join(lineList[:-1]) + ' {};' + r"'.format(params['" + key + r"'])"
    d[key] = default
    return r"r'" + line

def findStars(lines):
    pattern = re.compile(".*\* \* \*.*")
    for i, line in enumerate(lines):
        if pattern.match(line) is not None:
            return i + 1




def makeFillFile(rez, fd=None, fp=None):
    f = filePointer(fd=fd, fp=fp)
    rez = filePointer(fd=rez, flag='w')
    lines = f.readlines()
    f.close()
    d = {}
    lines = lines[7:]
    bound = findStars(lines)
    for i, line in enumerate(lines):
        if i < bound:
            print('    ', r"r'" + line[:-1] + r"' + '\n' " + '+ \\', file=rez)
            continue
        line = searchParam(line[:-1], d)
        if i == len(lines) - 1:
            print('    ', line + r" + '\n '", file=rez)
        else:
            print('    ', line + r" + '\n' " + '+ \\', file=rez)
    rez.close()
    return (d)

def makeFillFileParams(rez, fd=None, fp=None):
    f = filePointer(fd=fd, fp=fp)
    rez = filePointer(fd=rez, flag='w')
    lines = f.readlines()
    f.close()
    d = {}
    lines = lines[7:]
    bound = 0
    for i, line in enumerate(lines):
        if i < bound:
            print('    ', r"r'" + line[:-1] + r"' + '\n' " + '+ \\', file=rez)
            continue
        line = searchParam(line[:-1], d)
        if i == len(lines) - 1:
            print('    ', line + r" + '\n '", file=rez)
        else:
            print('    ', line + r" + '\n' " + '+ \\', file=rez)
    rez.close()
    return (d)

def copyCleanFile(rez, fd=None, fp=None):
    f = filePointer(fd=fd, fp=fp)
    rez = filePointer(fd=rez, flag='w')
    lines = f.readlines()
    f.close()
    lines = lines[7:]
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print('    ', r"r'" + line[:-1] + r"' + '\n '", file=rez)
        else:
            print('    ', r"r'" + line[:-1] + r"' + '\n' " + '+ \\', file=rez)
    rez.close()
def findParts(lines):
    pattern1 = re.compile('.*\{.*')
    pattern2 = re.compile('.*\}.*')
    rez = []
    flag = False
    for i, line in enumerate(lines):
        if pattern1.match(line) is not None:
            tmp = {}
            tmp['key'] = lines[i - 1].split()[0]
            tmp['lbound'] = i
            flag = True
        if flag:
            if pattern2.match(line) is not None:
                tmp['rbound'] = i
                rez.append(tmp)
                flag = False
    return rez



def makeFillDuplicateNames(rez, fd=None, fp=None):
    f = filePointer(fd=fd, fp=fp)
    rez = filePointer(fd=rez, flag='w')
    lines = f.readlines()
    f.close()
    d = {}
    lines = lines[7:]
    bound = findStars(lines)
    parts = findParts(lines)
    for i, line in enumerate(lines):
        if i < bound:
            print('    ', r"r'" + line[:-1] + r"' + '\n' " + '+ \\', file=rez)
            continue
        if i == len(lines) - 1:
            line = searchParam(line[:-1], d)
            print('    ', line + r" + '\n '", file=rez)
        else:
            part = None
            for foo in parts:
                if i >= foo['lbound'] and i <= foo['rbound']:
                    part = foo
                    break
            line = searchParam(line[:-1], d, part)
            print('    ', line + r" + '\n' " + '+ \\', file=rez)
    rez.close()
    return (d)


dist = 'fill'
src_system = '../system'
src_constant = '../constant'
dist = Path(Path.cwd(), dist)
src1 = Path(Path.cwd(), src_system)
src2 = Path(Path.cwd(), src_constant)

shutil.rmtree(dist, ignore_errors=True)
os.mkdir(dist)

def makeFiles(src, dist):
    d = {}
    for name in os.listdir(src):
        if name == 'blockMeshDict':
            continue
        filename = os.path.join(src, name)
        if os.path.isfile(filename):
            path = Path(dist,name)
            rez = open(f'{path}.py', 'w')
            print(f'def fill_{name}(params):', '    return ', sep='\n', end='', file=rez)
            if name == 'fvSchemes' or name == 'fvSolution':
                dd = makeFillDuplicateNames(rez=rez, fp=filename)
            elif name =='setFieldsDict' or name == 'WENODict':
                copyCleanFile(rez=rez, fp=filename)
            elif name =='params':
                makeFillFileParams(rez=rez, fp=filename)
            else:
                dd = makeFillFile(rez=rez, fp=filename)
            d[name] = dd
    return d


d = {}
d['system'] = makeFiles(src1, dist)

d['constant'] = makeFiles(src2, dist)

f = open(Path(dist, 'parametres.py'), 'w')
print('filedata = ', d, file=f)
f.close()