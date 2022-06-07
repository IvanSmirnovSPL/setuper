def fill_alpha_water(params):
    return ' dimensions      [0 0 0 0 0]; '  + '\n' + \
 '  '  + '\n' + \
 ' internalField   uniform 1; '  + '\n' + \
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
 '         type            inletOutlet; '  + '\n' + \
 '         inletValue      $internalField; '  + '\n' + \
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
