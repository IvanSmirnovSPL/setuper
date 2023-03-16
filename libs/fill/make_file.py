import sys

path = sys.argv[1]

with open(path, 'r') as f:
    lines = f.readlines()
for line in lines:
    print(r"'" + line[:-1] + r"'" + r" + '\n' + " "\\")