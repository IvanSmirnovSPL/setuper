from libs.fields import Fields


def fill_alpha_water(params, fn=None, fp=None):
    alpha_water = Fields(field_name='alpha.water', internal_value=params['internal_value'],
                         boundary_types=params.get('boundary_types', None),
                         boundary_name=params.get('boundary_name', None),
                         value=params.get('value', None))
    alpha_water.make_boundary_conditions(filename=fn, fp=fp, value_name={'out_with_value': 'inletValue'})


'''return ' dimensions      {}; '.format(params['dimensions_alpha']) + '\n' + \
           '  ' + '\n' + \
           ' internalField   {}; '.format(params['internalField_alpha']) + '\n' + \
           '  ' + '\n' + \
           ' boundaryField ' + '\n' + \
           ' { ' + '\n' + \
           '     inlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_inlet_alpha']) + '\n' + \
           '         value           {}; '.format(params['value_inlet_alpha']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     outlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_outlet_alpha']) + '\n' + \
           '         inletValue      {}; '.format(params['inletValue_outlet_alpha']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     symmetry ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_alpha']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     wall ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_alpha']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
'''
