def fill_blockMeshDict(fd, path, params):
    file = open(path, 'a')
    keys = list(params.keys())
    file.write(fd.line())
    file.write(fd.string_with_spaces('scale', start_space=0))
    file.write(fd.line(str(params['scale']) + ';'))

    file.write(fd.line())
    file.write(fd.line('vertices'))
    file.write(fd.line('('))
    file.write('(0 0 0)' + '\n' + '(0.1 0 0)' + '\n' + '(0.1 0.1 0)' + '\n' +
               '(0 0.1 0)' + '\n' + '(0 0 0.01)' + '\n' + '(0.1 0 0.01)' + '\n' +
               '(0.1 0.1 0.01)' + '\n' + '(0 0.1 0.01)' + '\n')
    file.write(fd.line(');'))

    file.write(fd.line())
    file.write(fd.line('blocks'))
    file.write(fd.line('('))
    file.write('hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)' + '\n')
    file.write(fd.line(');'))

    file.write(fd.line())
    file.write(fd.line('edges'))
    file.write(fd.line('('))
    file.write(fd.line(');'))

    file.write(fd.line())
    file.write(fd.line('boundary'))
    file.write(fd.line('('))

    file.write(fd.line('movingWall'))
    file.write(fd.line('{'))
    file.write(fd.line(' type wall;'))
    file.write(fd.line(' faces'))
    file.write(fd.line(' ('))
    file.write(fd.line(' (3 7 6 2)'))
    file.write(fd.line(' );'))
    file.write(fd.line('}'))

    file.write(fd.line('fixedWalls'))
    file.write(fd.line('{'))
    file.write(fd.line(' type wall;'))
    file.write(fd.line(' faces'))
    file.write(fd.line(' ('))
    file.write(fd.line(' (0 4 7 3)'))
    file.write(fd.line(' (2 6 5 1)'))
    file.write(fd.line(' (1 5 4 0)'))
    file.write(fd.line(' );'))
    file.write(fd.line('}'))

    file.write(fd.line('frontAndBack'))
    file.write(fd.line('{'))
    file.write(fd.line(' type empty;'))
    file.write(fd.line(' faces'))
    file.write(fd.line(' ('))
    file.write(fd.line(' (0 3 2 1)'))
    file.write(fd.line(' (4 5 6 7)'))
    file.write(fd.line(' );'))
    file.write(fd.line('}'))

    file.write(fd.line(');'))

    file.write(fd.separator)
    file.close()
