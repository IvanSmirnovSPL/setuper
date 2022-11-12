import os

def copyCleanFile(rez, f):
    lines = f.readlines()
    f.close()
    lines = lines[7:]
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print('    ', r"r'" + line[:-1] + r"' + '\n '", file=rez)
        else:
            print('    ', r"r'" + line[:-1] + r"' + '\n' " + '+ \\', file=rez)
    rez.close()

path = r'/home/ivan/Documents/TSAGI/newFaKTFoamCase/src'
path1 = r'/home/ivan/Documents/TSAGI/newFaKTFoamCase/dist'

for filename in os.listdir(path):
    with open(path + '/' + filename, 'r') as f:
        with open(path1 + '/' + filename, 'w') as rez:
            copyCleanFile(rez, f)