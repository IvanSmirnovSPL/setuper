from libs.fields import Fields


def fill_p_rgh(params, fn=None, fp=None):
    BT = []
    for B in params.get('boundary_types', None):
        if B == 'wall':
            B = 'wall_pressure'
        if B == 'in_with_value':
            B = 'in_with_value_pressure'
        BT.append(B)

    p_rgh = Fields(field_name='p_rgh', internal_value=params.get('internal_value', None),
                   boundary_types=BT,
                   boundary_name=params.get('boundary_name', None),
                   value=params.get('value', None))
    p_rgh.make_boundary_conditions(filename=fn, fp=fp)


'''return ' dimensions     {}; '.format(params['dimensions_p_rgh']) + '\n' + \
           '  ' + '\n' + \
           ' internalField   {}; '.format(params['internalField_p_rgh']) + '\n' + \
           '  ' + '\n' + \
           ' boundaryField ' + '\n' + \
           ' { ' + '\n' + \
           '     inlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_inlet_p_rgh']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     outlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_outlet_p_rgh']) + '\n' + \
           '         value           {}; '.format(params['value_outlet_p_rgh']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     symmetry ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_p_rgh']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     walls ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_p_rgh']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
'''
