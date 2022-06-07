def fill_p_rgh (params):
    return ' dimensions      [1 -1 -2 0 0]; ' + '\n' + \
 '  '  + '\n' + \
 ' internalField   uniform 100000; '  + '\n' + \
 '  '  + '\n' + \
 ' boundaryField '  + '\n' + \
 ' { '  + '\n' + \
 '     inlet '  + '\n' + \
 '     { '  + '\n' + \
 '         type            zeroGradient; '  + '\n' + \
 '     } '  + '\n' + \
 '  '  + '\n' + \
 '     outlet '  + '\n' + \
 '     { '  + '\n' + \
 '         type            fixedValue; '  + '\n' + \
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
 '         type            fixedFluxPressure; '  + '\n' + \
 '     } '  + '\n' + \
 ' } '
