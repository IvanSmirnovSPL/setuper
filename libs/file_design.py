class FileDesign:

    def __init__(self):
        self.preamble = '/*--------------------------------*- C++ -*----------------------------------*\\' + '\n' + \
                        r'| =========                 |                                                 |' + '\n' + \
                        r'| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |' + '\n' + \
                        r'|  \\    /   O peration     | Version:  v2106                                 |' + '\n' + \
                        r'|   \\  /    A nd           | Website:  www.openfoam.com                      |' + '\n' + \
                        r'|    \\/     M anipulation  |                                                 |' + '\n' + \
                        r'\*---------------------------------------------------------------------------*/' + '\n'

        self.separator = r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n'

    def init_file(self, filename):
        file = open(filename, 'w')
        file.write(self.preamble)
        file.close()

    @staticmethod
    def line(string=''):
        return string + '\n'

    @staticmethod
    def string_with_spaces(string, start_space=4, length=16):
        end_space = length - len(string) - start_space
        end_space = end_space if end_space > 0 else 1
        return ' ' * start_space + string + ' ' * end_space

    def foamfile(self, path, version_='2.0', format_='ascii', class_='dictionary', object_=''):
        file = open(path, 'a')
        file.write(self.line('FoamFile'))
        file.write(self.line('{'))
        file.write(self.string_with_spaces('version'))
        file.write(self.line(version_ + ';'))
        file.write(self.string_with_spaces('format'))
        file.write(self.line(format_ + ';'))
        file.write(self.string_with_spaces('class'))
        file.write(self.line(class_ + ';'))
        file.write(self.string_with_spaces('object'))
        file.write(self.line(object_ + ';'))
        file.write(self.line('}'))
        file.write(self.separator)
        file.close()

    def part_of_dictionary(self, params, part_name, file, start_space=0, length=16):
        file.write(self.line())
        file.write(self.string_with_spaces(part_name, start_space=start_space, length=length))
        file.write(self.line(str(params[part_name]) + ';'))

    def part_of_dict_is_dict(self, params, part_name, file, start_space=0, length=16):
        file.write(self.line())
        file.write(self.line(self.string_with_spaces(part_name, start_space=start_space, length=length)))
        dictionary = params[part_name]
        file.write(self.line(' '*start_space + '{'))
        for key in dictionary.keys():
            tmp = dictionary[key]
            if type(tmp) is dict:
                self.part_of_dict_is_dict(dictionary, key, file, start_space=start_space + 4, length=length)
            elif type(tmp) is tuple:
                self.part_of_dict_is_tuple(dictionary, key, file, start_space=start_space + 4, length=length)
            else:
                self.part_of_dictionary(dictionary, key, file, start_space=start_space + 4, length=length)
        file.write(self.line(' '*start_space + '}'))


    def part_of_dict_is_tuple(self, params, part_name, file, start_space=0, length=16):
        file.write(self.line())
        file.write(self.line(self.string_with_spaces(part_name, start_space=start_space, length=length)))
        dictionary = params[part_name][0]
        file.write(self.line('('))
        for key in dictionary.keys():
            tmp = dictionary[key]
            if type(tmp) is dict:
                self.part_of_dict_is_dict(dictionary, key, file, start_space=start_space + 4, length=length)
            elif type(tmp) is tuple:
                self.part_of_dict_is_tuple(dictionary, key, file, start_space=start_space + 4, length=length)
            else:
                self.part_of_dictionary(dictionary, key, file, start_space=start_space + 4, length=length)
        file.write(self.line(');'))


