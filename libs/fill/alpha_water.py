def fill_alpha_water(params):
    return ' dimensions      {}; '.format(params['dimensions_alpha']) + '\n' + \
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
           '     walls ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_walls_alpha']) + '\n' + \
           '     } ' + '\n' + \
           '  ' + '\n' + \
           '     bullet ' + '\n' + \
           '     { ' + '\n' + \
           '         type            {}; '.format(params['type_bullet_alpha']) + '\n' + \
           '     } ' + '\n' + \
           ' } '
