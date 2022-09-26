

class Argument:
    def __init__(self, _type, _name, _value, _default, _help):
        self.type = _type
        self.name = _name
        self.value = _value
        self.default = _default
        self.help = _help


def fillArgument(arg):
    if arg.type == 'str':
        rez = r'"' + arg.name + r'"' + ' : {' + '\n' + \
              '"value": ' + '"' + arg.default + '"' +', \n' + \
              '"default":' + '"' + arg.default + '"' + ', \n' + \
              '"descripetion": "' + arg.help + '"' + ', \n' + \
              '"option":' + '"' + arg.value + '"' + ', \n' + \
              '"importance": 2 \n' + \
              '}, \n'
    if arg.type == 'int':
        rez = r'"' + arg.name + r'"' + ' : {' + '\n' +\
            '"value": ' + arg.default + ', \n' +\
            '"default":' + arg.default + ', \n' +\
            '"min":' + arg.default + ', \n' +\
            '"max":' + arg.default + ', \n' +\
            '"descripetion": "' + arg.help +'"' + ', \n' +\
            '"option":' + '"' + arg.value + '"' + ', \n' +\
            '"importance": 2 \n' +\
        '}, \n'
    return rez
def detectArgument(path):
    rez = []
    with open(path, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        cur = ''
        if line.find('.add_argument(') > -1:
            cur += line[line.find('.add_argument(') + 14: -2]
        if line.find('help') == -1:
            while lines[i + 1].find('help') == -1:
                cur += lines[i][-2] + lines[i + 1][:-1]
                i += 1
            cur += lines[i][-2] + lines[i + 1][ : -2]
            i += 1
        i += 1
        tmp = cur.split(', ')
        arg = Argument(_value=tmp[0][1:-1], _name=tmp[1][3:-1], _type=tmp[3][5:], _default=tmp[4][9:-1],
                       _help=tmp[-1][tmp[-1].find('=') + 2: -1])
        if arg.default.isdigit():
            arg.type = 'int'
        rez.append(arg)

    return rez

rez = detectArgument('prop.txt')
with open('new.txt', 'w') as f:
    for r in rez:
        f.write(fillArgument(r))