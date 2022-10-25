import re
import os
import shutil
from pathlib import Path


preamble = '/*--------------------------------*- C++ -*----------------------------------*\\' + '\n' + \
            r'| =========                 |                                                 |' + '\n' + \
            r'| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |' + '\n' + \
            r'|  \\    /   O peration     | Version:  v2106                                 |' + '\n' + \
            r'|   \\  /    A nd           | Website:  www.openfoam.com                      |' + '\n' + \
            r'|    \\/     M anipulation  |                                                 |' + '\n' + \
            r'\*---------------------------------------------------------------------------*/' + '\n'

def filePointer(fd=None, fp=None, flag='r'):
    if fp is not None:
        f = open(fp, flag)
    else:
        f = fd
    return f

def searchParam(line, d):
    tmp = line.rfind(';')
    if tmp == -1:
        return r"'" + line + r"'"
    foo = line[:tmp].rfind(' ')
    bar = line.find('  ')
    default = line[foo: tmp]
    key = line[:bar + 1].replace(' ', '')
    line = line[:foo] + r" {};'.format(params['" + key + r"'])"
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
            print('    ', r"r'" + line[:-1] + r"' + '\n' " + ' + \\', file=rez)
            continue
        line = searchParam(line[:-1], d)
        if i == len(lines) - 1:
            print('    ', line + r" + '\n '", file=rez)
        else:
            print('    ', line + r" + '\n' " + ' + \\', file=rez)
    rez.close()
    return (d)


dist = 'fill'
src = 'system'
dist = Path(Path.cwd(), dist)
src = Path(Path.cwd(), src)

shutil.rmtree(dist, ignore_errors=True)
os.mkdir(dist)

def makeFiles(src, dist):
    d = {}
    for name in os.listdir(src):
        filename = os.path.join(src, name)
        if os.path.isfile(filename):
            path = Path(dist,name)
            rez = open(f'{path}.py', 'w')
            print(f'def fill_{name}(params):', '    return ', sep='\n', end='', file=rez)
            dd = makeFillFile(rez=rez, fp=filename)
            d[name] = dd
    return d


d = makeFiles(src, dist)
print(d)