file_ = open('test', 'r')

for line in file_:
    #print(" ' ", line, " ' ", " + '\n' ", " + \ ")
    print(" ' ", end='')
    print(line[:-1], end='')
    print(" ' ", end='')
    print(" + '\\n' + \\")
