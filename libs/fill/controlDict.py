def fill_controlDict(params):
    return '  '  + '\n' + \
 ' application     interPhaseChangeFoam; '  + '\n' + \
 '  '  + '\n' + \
 ' startFrom       latestTime; '  + '\n' + \
 '  '  + '\n' + \
 ' startTime       0; '  + '\n' + \
 '  '  + '\n' + \
 ' stopAt          endTime; '  + '\n' + \
 '  '  + '\n' + \
 ' endTime         0.05; '  + '\n' + \
 '  '  + '\n' + \
 ' deltaT          1e-8; '  + '\n' + \
 '  '  + '\n' + \
 ' writeControl    adjustable; '  + '\n' + \
 '  '  + '\n' + \
 ' writeInterval   0.001; '  + '\n' + \
 '  '  + '\n' + \
 ' purgeWrite      0; '  + '\n' + \
 '  '  + '\n' + \
 ' writeFormat     ascii; '  + '\n' + \
 '  '  + '\n' + \
 ' writePrecision  6; '  + '\n' + \
 '  '  + '\n' + \
 ' writeCompression off; '  + '\n' + \
 '  '  + '\n' + \
 ' timeFormat      general; '  + '\n' + \
 '  '  + '\n' + \
 ' runTimeModifiable yes; '  + '\n' + \
 '  '  + '\n' + \
 ' adjustTimeStep  on; '  + '\n' + \
 '  '  + '\n' + \
 ' maxCo           5; '
