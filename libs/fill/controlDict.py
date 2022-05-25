def fill_cohntrolDict(fd, path, params):
    file = open(path, 'a')
    keys = list(params.keys())
    for key in keys:
        fd.part_of_dictionary(params, key, file)
    file.write(fd.line())
    file.write(fd.separator)
    file.close()