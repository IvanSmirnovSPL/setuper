def fill_controlDict(params):
    return '  ' + '\n' + \
           ' application     interPhaseChangeFoam; ' + '\n' + \
           '  ' + '\n' + \
           ' startFrom       {}; '.format(params['startFrom']) + '\n' + \
           '  ' + '\n' + \
           ' startTime       {}; '.format(params['startTime']) + '\n' + \
           '  ' + '\n' + \
           ' stopAt          {}; '.format(params['stopAt']) + '\n' + \
           '  ' + '\n' + \
           ' endTime         {}; '.format(params['endTime']) + '\n' + \
           '  ' + '\n' + \
           ' deltaT          {}; '.format(params['deltaT']) + '\n' + \
           '  ' + '\n' + \
           ' writeControl    {}; '.format(params['writeControl']) + '\n' + \
           '  ' + '\n' + \
           ' writeInterval   {}; '.format(params['writeInterval']) + '\n' + \
           '  ' + '\n' + \
           ' purgeWrite      {}; '.format(params['purgeWrite']) + '\n' + \
           '  ' + '\n' + \
           ' writeFormat     {}; '.format(params['writeFormat']) + '\n' + \
           '  ' + '\n' + \
           ' writePrecision  {}; '.format(params['writePrecision']) + '\n' + \
           '  ' + '\n' + \
           ' writeCompression {}; '.format(params['writeCompression']) + '\n' + \
           '  ' + '\n' + \
           ' timeFormat      {}; '.format(params['timeFormat']) + '\n' + \
           '  ' + '\n' + \
           ' runTimeModifiable {}; '.format(params['runTimeModifiable']) + '\n' + \
           '  ' + '\n' + \
           ' adjustTimeStep  {}; '.format(params['adjustTimeStep']) + '\n' + \
           '  ' + '\n' + \
           ' maxCo           {}; '.format(params['maxCo'])
