def fill_Phi(params):
    return ' dimensions      {}; '.format(params['dimensions_Phi']) + '\n' + \
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
           '     walls ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_Phi']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     bullet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_Phi']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
