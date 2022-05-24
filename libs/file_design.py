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
        end_space = end_space if end_space > 0 else 0
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