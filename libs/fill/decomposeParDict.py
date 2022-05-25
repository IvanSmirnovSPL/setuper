def fill_decomposeParDict(fd, path, params):
    file = open(path, 'a')
    keys = list(params.keys())
    for key in keys[:-1]:
        fd.part_of_dictionary(params, key, file)
    fd.part_of_dict_is_dict(params, keys[-1], file)
    file.write(fd.line())
    file.write(fd.separator)
    file.close()