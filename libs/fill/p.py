def fill_p(fd, path, params):
    file = open(path, 'a')
    keys = list(params.keys())
    for key in keys:
        if type(params[key]) is dict:
            fd.part_of_dict_is_dict(params, key, file)
        elif type(params[key]) is tuple:
            fd.part_of_dict_is_tuple(params, key, file)
        else:
            fd.part_of_dictionary(params, key, file)
    file.write(fd.line())
    file.write(fd.separator)
    file.close()