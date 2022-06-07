def fill_U(params):
    return ' dimensions      [0 1 -1 0 0]; '  + '\n' + \
 '  '  + '\n' + \
 ' internalField   uniform (0 0 20); '  + '\n' + \
 '  '  + '\n' + \
 ' boundaryField '  + '\n' + \
 ' { '  + '\n' + \
 '     inlet '  + '\n' + \
 '     { '  + '\n' + \
 '         type            fixedValue; '  + '\n' + \
 '         value           $internalField; '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     outlet '  + '\n' + \
 '     { '  + '\n' + \
 '         type            pressureInletOutletVelocity; '  + '\n' + \
 '         value           $internalField; '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     walls '  + '\n' + \
 '     { '  + '\n' + \
 '         type            symmetry; '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     bullet '  + '\n' + \
 '     { '  + '\n' + \
 '         type            noSlip; '  + '\n' + \
 '     } '  + '\n' + \
 ' } '
