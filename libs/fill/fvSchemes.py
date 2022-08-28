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
           '     div(tauMC)      Gauss {}; \n'.format(param['div(tauMC)']) + \
           ' } \n' + \
           '  \n' + \
           ' laplacianSchemes \n' + \
           ' { \n' + \
           '     default         Gauss {}; \n'.format(param['laplacianSchemes']) + \
           ' } \n' + \
           '  \n' + \
           ' interpolationSchemes \n' + \
           ' { \n' + \
           '     default         {}; \n'.format(param['interpolationSchemes']) + \
           '  \n' + \
           '     reconstruct(U)      {}; \n'.format(param['reconstruct_U']) + \
           '  \n' + \
           '     reconstruct(p)      {}; \n'.format(param['reconstruct_p']) + \
           '     reconstruct(thermo:rho)    {}; \n'.format(param['reconstruct_thermo']) + \
           ' } \n' + \
           '  \n' + \
           ' snGradSchemes \n' + \
           ' { \n' + \
           '     default         {}; \n'.format(param['snGradSchemes']) + \
           ' } \n' + \
           '  \n'
