def fill_transportProperties(fd, path, params):
    file = open(path, 'a')
    file.write(fd.line())
    keys = list(params.keys())
    file.write(fd.string_with_spaces(keys[0], start_space=0))
    file.write(fd.line(str(params['nu']) + ';'))
    file.write(fd.line())
    file.write(fd.separator)
    file.close()