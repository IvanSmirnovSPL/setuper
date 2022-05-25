def fill_fvSchemes(fd, path, params):
    file = open(path, 'a')
    keys = list(params.keys())
    for key in keys:
        fd.part_of_dict_is_dict(params, key, file)
    file.write(fd.line())
    file.write(fd.separator)
    file.close()