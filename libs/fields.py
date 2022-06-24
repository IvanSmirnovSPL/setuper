import copy


class Boundary:
    def __init__(self, name='', parse_name='', value=False):
        self.name = name
        self.value = value
        self.parse_name = parse_name


dimensions = {'p': '[1 -1 -2 0 0 0 0]',
              'p_rgh': '[1 -1 -2 0 0 0 0]',
              'T': '[0 0 0 1 0 0 0]',
              'U': '[0 1 -1 0 0 0 0]',
              'Phi': '[0 2 -1 0 0 0 0]',
              'other': '[0 0 0 0 0 0 0]'}
# dictionary of boundary types, which consists of boundary names and other information
boundaries_types = {
    'wall': Boundary('noSlip', "(wall|WALL|Wall|originalPatch|Created).*"),
    'empty': Boundary('empty', "(empty|bottomEmpty|topEmpty).*"),
    'symmetry': Boundary('symmetry', "(symmetry).*"),
    'overset': Boundary('overset', "(overset).*"),
    'wedge': Boundary('wedge', "(wedge).*"),
    'slip': Boundary('slip', "(slip).*"),
    'symmetryPlane': Boundary('symmetryPlane', "(symmetryPlane).*"),
    'out': Boundary('zeroGradient', "(out|OUT|Out|sides).*"),
    'out_with_value': Boundary('fixedValue', "(outlet).*", value=True),
    'in': Boundary('zeroGradient', "(in|IN|In|otherSide).*"),
    'in_with_value': Boundary('fixedValue', "(inlet).*", value=True)
}


class Fields:

    def __init__(self, field_name, internal_value, boundary_types=None,
                                 boundary_name=None, value=None):
        self.dimensions = dimensions
        self.boundaries = boundaries_types
        self.field_name = field_name
        self.internal_value = internal_value
        self.boundary_types = boundary_types
        self.boundary_name = boundary_name
        self.value = value

    def write_field_type(self, field):
        if field in self.dimensions:
            return 'dimensions      {}; \n'.format(self.dimensions[field])
        else:
            return 'dimensions      {}; \n'.format(self.dimensions['other'])

    @staticmethod
    def write_internal_field(value=''):
        return 'internalField   uniform {};\n'.format(value)

    def write_condition(self, boundary_type, boundary_name=None, value=None, value_name='value'):
        tmp = copy.copy(self.boundaries[boundary_type])
        if boundary_name is not None:
            tmp.name = boundary_name
        if value is not None:
            tmp.value = value
        if tmp.value:
            return '"{0.parse_name}" \n{{ \n type      {0.name};\n {1}     {0.value}; \n}}\n'.format(tmp, value_name)
        else:
            return '"{0.parse_name}" \n{{ \n  type      {0.name};\n}}\n'.format(tmp)

    def make_boundary_conditions(self, filename=None, fp=None, value_name=None):
        if fp is None:
            f = open(filename, 'a')
        else:
            f = fp
        f.write(self.write_field_type(self.field_name))
        f.write(self.write_internal_field(self.internal_value))
        f.write('boundaryField \n{ \n ')
        if self.boundary_types is not None:
            tmp = self.boundary_types
        else:
            tmp = self.boundaries
        for boundary in tmp:
            bn = None
            v = None
            if self.boundary_name is not None and boundary in self.boundary_name.keys():
                bn = self.boundary_name[boundary]
            if self.value is not None and boundary in self.value.keys():
                v = self.value[boundary]
            vn = 'value'
            if value_name is not None and boundary in value_name.keys():
                vn = value_name[boundary]
            f.write(self.write_condition(boundary, bn, v, value_name=vn))
        f.write('}\n')
        f.close()


'''U = Fields(field_name='U', internal_value='(0 0 20)',
           boundary_types=['in_with_value', 'out_with_value', 'symmetry', 'wall'],
           boundary_name={'out_with_value': 'pressureInletOutletVelocity'},
           value={'in_with_value': '$internalField', 'out_with_value': '$internalField'})
U.make_boundary_conditions('/home/ivan/Documents/TEST_OpenFoam/setuper/test.txt')'''
