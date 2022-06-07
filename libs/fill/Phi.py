def fill_Phi(params):
    return ' dimensions      [0 2 -1 0 0]; '  + '\n' + \
 '  '  + '\n' + \
 ' internalField   uniform 0; '  + '\n' + \
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
 '         type            zeroGradient; '  + '\n' + \
 '     } '  + '\n' + \
 ' } '