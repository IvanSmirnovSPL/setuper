def fill_controlDict(param):
    return '  \n' + \
           'libs ' + r'( "' + param['libs']  + r'" );' + '\n' + \
           ' application     {}; \n'.format(param['application']) + \
           '  \n' + \
           ' startFrom       {}; \n'.format(param['startFrom']) + \
           '  \n' + \
           ' startTime       {}; \n'.format(param['startTime']) + \
           '  \n' + \
           ' stopAt          {}; \n'.format(param['stopAt']) + \
           '  \n' + \
           ' endTime         {}; \n'.format(param['endTime']) + \
           '  \n' + \
           ' deltaT          {}; \n'.format(param['deltaT']) + \
           '  \n' + \
           ' writeControl    {}; \n'.format(param['writeControl']) + \
           '  \n' + \
           ' writeInterval   {}; \n'.format(param['writeInterval']) + \
           '  \n' + \
           ' purgeWrite      {}; \n'.format(param['purgeWrite']) + \
           '  \n' + \
           ' writeFormat     {}; \n'.format(param['writeFormat']) + \
           '  \n' + \
           ' writePrecision  {}; \n'.format(param['writePrecision']) + \
           '  \n' + \
           ' writeCompression {}; \n'.format(param['writeCompression']) + \
           '  \n' + \
           ' timeFormat      {}; \n'.format(param['timeFormat']) + \
           '  \n' + \
           ' timePrecision   {}; \n'.format(param['timePrecision']) + \
           '  \n' + \
           ' runTimeModifiable {}; \n'.format(param['runTimeModifiable']) + \
           '  \n' + \
           ' adjustTimeStep  {}; \n'.format(param['adjustTimeStep']) + \
           '  \n' + \
           ' maxCo           {}; \n'.format(param['maxCo']) + \
           '  \n' + \
           ' maxDeltaT       {}; \n'.format(param['maxDeltaT']) + \
           '  \n'
