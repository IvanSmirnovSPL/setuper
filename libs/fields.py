import copy

'''
Field boundary condition structure( [...] means optional ):

<parse_name>
{
    type <name>
    [value <value>]
}

option 'value' may be another, for example 'inletValue',
thus it can be changed by dictionary parameter <value_name>:
{<boundary_type>: <vn>}
'''

'''
class Boundary() have information of specific boundary_type:
-- parse_name [String] - the template, which is parsing in mesh
-- name [String] - name of type 
-- value [Bool] - is value option necessary for this condition
'''


class Boundary:
    def __init__(self, name='', parse_name='', linearBC=False, t0=0, tf=0, v0=0, vf=0,  value=False):
        self.name = name
        self.value = value
        self.parse_name = parse_name
        self.linearBC = linearBC
        self.t0 = t0
        self.tf = tf
        self.v0 = v0
        self.vf = vf


'''dictionary of fields and its' dimensions'''
dimensions = {'p': '[1 -1 -2 0 0 0 0]',
              'p_rgh': '[1 -1 -2 0 0 0 0]',
              'T': '[0 0 0 1 0 0 0]',
              'U': '[0 1 -1 0 0 0 0]',
              'Phi': '[0 2 -1 0 0 0 0]',
              'other': '[0 0 0 0 0 0 0]'}

'''dictionary of boundary types, every boundary type is class Boundary()'''
# boundaries_ = {
#     'wall': Boundary('noSlip', "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*"),
#     'wall_pressure': Boundary('fixedFluxPressure', "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*"),
#     'wall_alpha': Boundary('zeroGradient', "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*"),
#     'in_with_value_pressure': Boundary('zeroGradient', "(inlet).*"),
#     'empty': Boundary('empty', "(empty|bottomEmpty|topEmpty).*"),
#     'symmetry': Boundary('symmetry', "(symmetry).*"),
#     'overset': Boundary('overset', "(overset).*"),
#     'wedge': Boundary('wedge', "(wedge).*"),
#     'slip': Boundary('slip', "(slip).*"),
#     'symmetryPlane': Boundary('symmetryPlane', "(symmetryPlane).*"),
#     'out': Boundary('zeroGradient', "(out|OUT|Out|sides).*"),
#     'out_with_value': Boundary('fixedValue', "(outlet).*", value=True),
#     'in': Boundary('zeroGradient', "(in|IN|In|otherSide).*"),
#     'in_with_value': Boundary('fixedValue', "(inlet).*", value=True)
# }

boundaries = {
    'wall_velocity': Boundary('noSlip', "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*"),
    'wall_alpha': Boundary('zeroGradient', "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*"),
    'wall_pressure': Boundary('zeroGradient', "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*"),
    'inlet_velocity': Boundary('fixedValue', "(inlet).*", value=True),
    'inlet_alpha': Boundary('fixedValue', "(inlet).*", value=True),
    'inlet_pressure': Boundary('zeroGradient', "(inlet).*"),
    'outlet_velocity': Boundary('zeroGradient', "(outlet).*"),
    'outlet_alpha': Boundary('zeroGradient', "(outlet).*"),
    'outlet_pressure': Boundary('fixedValue', "(outlet).*", value=True),
    'symmetry': Boundary('symmetry', "(symmetry).*"),
    'wedge': Boundary('wedge', "(wedge).*"),
}


def refactorTypes(types):
    for idt, type in enumerate(types):
        if type == ('outlet' or 'Outlet' or 'OUTLET'):
            types[idt] = 'out_with_value'
        if type == ('inlet' or 'Inlet' or 'INLET'):
            types[idt] = 'in_with_value'
        if type == ('empty' or 'Empty' or 'EMPTY'):
            types[idt] = 'empty'
        if type == 'walls':
            types[idt] = 'wall'
    return types


'''
class Fields:

#
__init__(field_name, internal_value, boundary_types=None,
                 boundary_name=None, value=None)
Input:
-- field_name [String] - field name from dimensions dictionary
-- internal value [String] - internal field value
-- boundary_types [List of String] - list of boundaries, which is necessary fill
                                                       for this field
-- boundary_name [Dictionary of String] - list of boundary names
(if it is necessary to change [type <name>] for some boundaries from boundary_types list)
-- value [Dictionary of String] - list of values for boundaries, which require them 

#
write_field_type(field)
Input:
-- field [String] - fild from dimensions dictionary
Output:
[String] dimension line

#
write_internal_field(field)
Input:
-- field [String] - fild from dimensions dictionary
Output:
[String] internal_field line 

#
write_condition(boundary_type, boundary_name=None, value=None, value_name='value')
Input:
-- boundary_type [String] - boundary type from boundaries dictionary
-- boundary_name [String] - optional parameter if it is necessary to change
                                            default [type <name>] for this boundary 
-- value [String] - optional parameter if boundary requires value
-- value_name [String] - optional parameter if it is necessary to change 'value' for smth
Output:
[String] line in Field boundary condition structure

#
make_boundary_conditions(filename=None, fp=None, value_name=None)
Input:
-- filename [Path/String] - path to output file(where write field info)
-- fp [File pointer] - open(filename) object
-- value [Dictionary of String] - if it is necessary to change 'value' in some boundaries
(filename or fp interchangeable)
Output: nothing
'''


class Fields:

    def __init__(self, field_name, internal_value, boundary_types=None,
                 boundary_name=None, value=None, advantageBC=None):
        self.dimensions = dimensions
        self.boundaries = boundaries
        self.field_name = field_name
        self.internal_value = internal_value
        self.boundary_types = boundary_types
        self.boundary_name = boundary_name
        self.value = value
        self.advantageBC = advantageBC

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
        if boundary_type.find('_') != -1:
            name = boundary_type[:boundary_type.find('_')]
            print(name)
            if self.advantageBC is not None and self.advantageBC['linearBC'] is True and name in self.advantageBC['faces']:
                foo = self.advantageBC
                if str(foo['vo']).find('_') == -1:
                    return '\n' + str(
                        tmp.parse_name) + '\n{\n \t type            uniformFixedValue; \n \t uniformValue    table ' + f"(({foo['to']} {foo['vo']}) ({foo['tf']} {foo['vf']}));" + ' \n}\n'
                else:
                    vo = '(' + str(foo['vo']).replace('_', ' ') + ')'
                    vf = '(' + str(foo['vf']).replace('_', ' ') + ')'
                    return '\n' + str(tmp.parse_name) + '\n{\n \t type            uniformNormalFixedValue; \n \t uniformValue    table ' + f"(({foo['to']} {vo}) ({foo['tf']} {vf}));" + ' \n}\n'
        if boundary_name is not None:
            tmp.name = boundary_name
        if value is not None:
            tmp.value = value
        if value is True:
            tmp.value = '$internalField'
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
