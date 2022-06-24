from libs.fields import Fields


def fill_p_rgh(params, fn=None, fp=None):
    p_rgh = Fields(field_name='p_rgh', internal_value=params['internal_value'],
                   boundary_types=params['boundary_types'],
                   boundary_name=params['boundary_name'],
                   value=params['value'])
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
