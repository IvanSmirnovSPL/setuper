def makeFile(d, name, rezPath):
    keys = d.keys()
    with open(rezPath, 'w') as f:
        for key in keys:
            print(f'{key} = ' + f'\\',file=f)
            showDict(key=key, d=d[key], delta=1, f=f)
        line = [r"'" + key_ + r"': " + key_ for key_ in keys]
        print(f'{name} = ' +r"{" + ", ".join(line) + r"}", file=f)


def showDict(key, d, delta, f):
    if not isinstance(d, dict):
        print('\t'*delta + r"'" + key + r"': " + r"'" + d + r"',",  file=f)
    else:
        print('\t'*delta + r'{', file=f)
        for key_ in d.keys():
            if isinstance(d[key_], dict):
                print('\t' * (delta + 1) + r"'" + key_ + r"': ", file=f)
            showDict(key_, d[key_], delta=delta + 1, f=f)
        print('\t' * delta + r'}, ', file=f)





