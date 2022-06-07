def fill_blockMeshDict(params):
   return '  '  + '\n' + \
 ' scale   0.001; '  + '\n' + \
 '  '  + '\n' + \
 ' vertices '  + '\n' + \
 ' ( '  + '\n' + \
 '     (-15 -15 -15) '  + '\n' + \
 '     (15 -15 -15) '  + '\n' + \
 '     (15  15 -15) '  + '\n' + \
 '     (-15  15 -15) '  + '\n' + \
 '     (-15 -15 100) '  + '\n' + \
 '     (15 -15 100) '  + '\n' + \
 '     (15  15 100) '  + '\n' + \
 '     (-15  15 100) '  + '\n' + \
 ' ); '  + '\n' + \
 '  '  + '\n' + \
 ' blocks '  + '\n' + \
 ' ( '  + '\n' + \
 '     hex (0 1 2 3 4 5 6 7) (15 15 50) simpleGrading (1 1 1) '  + '\n' + \
 ' ); '  + '\n' + \
 '  '  + '\n' + \
 ' boundary '  + '\n' + \
 ' ( '  + '\n' + \
 '     inlet '  + '\n' + \
 '     { '  + '\n' + \
 '         type patch; '  + '\n' + \
 '         faces '  + '\n' + \
 '         ( '  + '\n' + \
 '             (0 3 2 1) '  + '\n' + \
 '         ); '  + '\n' + \
 '     } '  + '\n' + \
 '     outlet '  + '\n' + \
 '     { '  + '\n' + \
 '         type patch; '  + '\n' + \
 '         faces '  + '\n' + \
 '         ( '  + '\n' + \
 '             (4 5 6 7) '  + '\n' + \
 '         ); '  + '\n' + \
 '     } '  + '\n' + \
 '     walls '  + '\n' + \
 '     { '  + '\n' + \
 '         type symmetry; '  + '\n' + \
 '         faces '  + '\n' + \
 '         ( '  + '\n' + \
 '             (0 4 7 3) '  + '\n' + \
 '             (2 6 5 1) '  + '\n' + \
 '             (1 5 4 0) '  + '\n' + \
 '             (3 7 6 2) '  + '\n' + \
 '         ); '  + '\n' + \
 '     } '  + '\n' + \
 ' ); '
