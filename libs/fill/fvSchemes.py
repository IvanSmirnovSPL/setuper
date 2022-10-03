def fill_fvSchemes(param):
    return '  \n' + \
           ' compressible \n' + \
           ' { \n' + \
           '     fluxScheme       {}; \n'.format(param['fluxScheme']) + \
           ' } \n' + \
           '  \n' + \
           ' ddtSchemes \n' + \
           ' { \n' + \
           '     default          {}; \n'.format(param['ddtSchemes']) + \
           '     fluxIntegrator   {}; \n'.format(param['fluxIntegrator']) + \
           ' } \n' + \
           '  \n' + \
           ' gradSchemes \n' + \
           ' { \n' + \
           '     default         Gauss {}; \n'.format(param['gradSchemes']) + \
           ' } \n' + \
           '  \n' + \
           ' divSchemes \n' + \
           ' { \n' + \
           '     default         {}; \n'.format(param['divSchemes']) + \
           '  \n' + \
           '     div(tauMC)      Gauss linear; \n'+ \
           '      div((S&U))      Gauss linear; \n' + \
           ' } \n' + \
           '  \n' + \
           ' laplacianSchemes \n' + \
           ' { \n' + \
           '     default         Gauss {}; \n'.format(param['laplacianSchemes']) + \
           ' } \n' + \
           '  \n' + \
           ' interpolationSchemes \n' + \
           ' { \n' + \
           '     default         none; \n' + \
           '     flux(U)         linear; \n' + \
           '     reconstruct(U)      upwind; \n' + \
           '     interpolate(thermo:c) upwind phi; \n' + \
           '     reconstruct(thermo:rho)    upwind; \n' + \
           '     reconstruct(thermo:he)    upwind; \n' + \
           ' } \n' + \
           '  \n' + \
           ' snGradSchemes \n' + \
           ' { \n' + \
           '     default         {}; \n'.format(param['snGradSchemes']) + \
           ' } \n' + \
           '  \n'
