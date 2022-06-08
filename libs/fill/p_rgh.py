def fill_p_rgh(params):
    return ' dimensions     {}; '.format(params['dimensions_p_rgh']) + '\n' + \
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
           '     walls ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_p_rgh']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     bullet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_p_rgh']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
