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

        self.clean = r'#!/bin/sh' + '\n' + \
                     'cd "${0%/*}" || exit                                # Run from this directory' + '\n' + \
                     '. ${WM_PROJECT_DIR:?}/bin/tools/CleanFunctions      # Tutorial clean functions' + '\n' + \
                     '#------------------------------------------------------------------------------' + '\n' + \
                     ' ' + '\n' + \
                     'cleanCase0' + '\n' + \
                     ' ' + '\n' + \
                     'rm -rf constant/triSurface' + '\n' + \
                     ' ' + '\n' + \
                     '#------------------------------------------------------------------------------'

        self.run = '#!/bin/sh' + '\n' + \
                   'cd "${0%/*}" || exit                                # Run from this directory' + '\n' + \
                   '. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions        # Tutorial run functions' + '\n' + \
                   '#------------------------------------------------------------------------------' + '\n' + \
                   ' ' + '\n' + \
                   'mkdir -p constant/triSurface' + '\n' + \
                   ' ' + '\n' + \
                   '# Copy bullet surface from resources directory' + '\n' + \
                   'cp -f \\' + '\n' + \
                   '    "$FOAM_TUTORIALS"/resources/geometry/bullet.stl.gz \\' + '\n' + \
                   r'    constant/triSurface/' + '\n' + \
                   ' ' + '\n' + \
                   '# Generate the base block mesh' + '\n' + \
                   'runApplication blockMesh' + '\n' + \
                   ' ' + '\n' + \
                   '# Generate the snappy mesh' + '\n' + \
                   'runApplication snappyHexMesh -overwrite' + '\n' + \
                   ' ' + '\n' + \
                   'restore0Dir' + '\n' + \
                   ' ' + '\n' + \
                   '# Initialise with potentialFoam solution' + '\n' + \
                   'runApplication potentialFoam -pName p_rgh -writephi' + '\n' + \
                   ' ' + '\n' + \
                   '# Run the solver' + '\n' + \
                   'runApplication $(getApplication)' + '\n' + \
                   ' ' + '\n' + \
                   '#------------------------------------------------------------------------------'

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
        file.write(self.line(' ' * start_space + '{'))
        for key in dictionary.keys():
            tmp = dictionary[key]
            if type(tmp) is dict:
                self.part_of_dict_is_dict(dictionary, key, file, start_space=start_space + 4, length=length)
            elif type(tmp) is tuple:
                if type(tmp[0]) is dict:
                    self.part_of_dict_is_tuple(dictionary, key, file, start_space=start_space + 4, length=length)
                else:
                    self.part_of_tuple_is_tuple(dictionary, key, file, start_space=start_space + 4, length=length)
            else:
                self.part_of_dictionary(dictionary, key, file, start_space=start_space + 4, length=length)
        file.write(self.line(' ' * start_space + '}'))

    def part_of_dict_is_tuple(self, params, part_name, file, start_space=0, length=16):
        if type(params[part_name][0]) is dict:
            file.write(self.line())
            file.write(self.line(self.string_with_spaces(part_name, start_space=start_space, length=length)))
            dictionary = params[part_name][0]
            file.write(self.line('('))
            for key in dictionary.keys():
                tmp = dictionary[key]
                if type(tmp) is dict:
                    self.part_of_dict_is_dict(dictionary, key, file, start_space=start_space + 4, length=length)
                elif type(tmp) is tuple:
                    if type(tmp[0]) is dict:
                        self.part_of_dict_is_tuple(dictionary, key, file, start_space=start_space + 4, length=length)
                    else:
                        self.part_of_tuple_is_tuple(dictionary, key, file, start_space=start_space + 4, length=length)
                else:
                    self.part_of_dictionary(dictionary, key, file, start_space=start_space + 4, length=length)
            file.write(self.line(');'))
        else:
            self.part_of_tuple_is_tuple(params, part_name, file, start_space=start_space, length=16)

    def part_of_tuple_is_tuple(self, params, part_name, file, start_space=0, length=16):
        file.write(self.line())
        file.write(self.line(self.string_with_spaces(part_name, start_space=start_space, length=length)))
        foo = params[part_name]
        file.write(self.line(' ' * start_space + '('))
        for tmp in foo:
            file.write(self.line(' ' * (4 + start_space) + tmp))
        file.write(self.line(' ' * start_space + ')'))
