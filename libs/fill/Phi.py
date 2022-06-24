from libs.fields import Fields


def fill_Phi(params, fn=None, fp=None):
       Phi = Fields(field_name='Phi', internal_value=params['internal_value'],
                      boundary_types=params['boundary_types'],
                      boundary_name=params['boundary_name'],
                      value=params['value'])
       Phi.make_boundary_conditions(filename=fn, fp=fp)

'''return ' dimensions      {}; '.format(params['dimensions_Phi']) + '\n' + \
           '  ' + '\n' + \
           ' internalField   {}; '.format(params['internalField_Phi']) + '\n' + \
           '  ' + '\n' + \
           ' boundaryField ' + '\n' + \
           ' { ' + '\n' + \
           '     inlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_inlet_Phi']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     outlet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_outlet_Phi']) + '\n' + \
           '         value           {}; '.format(params['value_outlet_Phi']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     symmetry ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_Phi']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     wall ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_Phi']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
'''