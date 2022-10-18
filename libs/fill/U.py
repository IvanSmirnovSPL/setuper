from libs.fields import Fields


def fill_U(params, fn=None, fp=None):
    U = Fields(field_name='U', internal_value=params.get('internal_value', None),
               boundary_types=params.get('boundary_types', None),
               boundary_name=params.get('boundary_name', None),
               value=params.get('value', None))
    U.make_boundary_conditions(filename=fn, fp=fp)


''' return ' dimensions      {}; '.format(params['dimensions_U']) + '\n' + \
           '  ' + '\n' + \
           ' internalField   {}; '.format(params['internalField_U']) + '\n' + \
           '  ' + '\n' + \
           ' boundaryField ' + '\n' + \
           ' { ' + '\n' + \
           '     inlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_inlet_U']) + '\n' + \
           '         value           {}; '.format(params['value_inlet_U']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     outlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_outlet_U']) + '\n' + \
           '         value           {}; '.format(params['value_outlet_U']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     walls ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_U']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     bullet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_U']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
'''
