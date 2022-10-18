from pathlib import Path
import re


def findCount(lines) -> (int, int, int):
    tmp_ = 0
    foo_ = 0
    for i, line in enumerate(lines):
        tmp = re.match(r"\(", line)
        foo = re.match(r"\)", line)
        if type(tmp) is not type(None):
            tmp_ = i
        if type(foo) is not type(None):
            foo_ = i
    return tmp_, foo_, int(lines[tmp_ - 1])


def findBoundaryTypes(lines):
    types = []
    top, low, num = findCount(lines)
    lines = lines[top + 1: low]
    for i in range(num):
        for i, line in enumerate(lines):
            tmp = re.match(r".*\{.*", line)
            if type(tmp) is not type(None):
                types.append(lines[i - 1][:-1].replace(" ", ""))
                lines = lines[i + 1:low]
                break
    return types


def detectBTypes(path):
    with open(Path(path, 'boundary'), 'r') as f:
        lines = f.readlines()
    return findBoundaryTypes(lines)