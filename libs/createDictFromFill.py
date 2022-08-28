name = 'thermophysicalProperties'

with open(f'./fill/{name}.py', 'r') as f:
    lines = f.readlines()
print(f" '{name}' : \n \t {{")
keys = []
for line in lines:
    line = str(line)
    if line.find('param[') != -1:
        key = line[line.find('param[') + 6: line.find('])')]
        if key not in keys:
            keys.append(key)
            print(f'\t \t {key} : 0,')
print(f'\t }},')