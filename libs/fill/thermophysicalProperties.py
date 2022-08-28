def fill_thermophysicalProperties(param):
    return '  \n' + \
           ' phases ( {} ); \n'.format(param['phases']) + \
           '  \n' + \
           ' Tmin {}; \n'.format(param['Tmin']) + \
           ' Tmax {}; \n'.format(param['Tmax']) + \
           '  \n' + \
           ' relTol {}; \n'.format(param['relTol']) + \
           ' maxIter {}; \n'.format(param['maxIter']) + \
           '  \n' + \
           '  \n' + \
           ' logPSatFile       {}; \n'.format(param['logPSatFile']) + \
           ' TSatFile       {}; \n'.format(param['TSatFile']) + \
           ' rho1SatFile    {}; \n'.format(param['rho1SatFile']) + \
           ' rho2SatFile    {}; \n'.format(param['rho2SatFile']) + \
           '  \n' + \
           ' rho1SatDerFile {}; \n'.format(param['rho1SatDerFile']) + \
           ' rho2SatDerFile {}; \n'.format(param['rho2SatDerFile']) + \
           '  \n' + \
           ' gvFile {}; \n'.format(param['gvFile']) + \
           ' glFile {}; \n'.format(param['glFile']) + \
           '  \n' + \
           ' TstepFile      {}; \n'.format(param['TstepFile']) + \
           '  \n' + \
           ' tables \n' + \
           ' { \n' + \
           ' } \n' + \
           '  \n'
