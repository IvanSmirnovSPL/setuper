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
           'default         none;//cellLimited<Venkatakrishnan> leastSquares 1.0;' + '\n' + \
           ' a cellLimited<Venkatakrishnan> leastSquares 1.0;' + '\n' + \
           'grad(thermo:rho) leastSquares;' + '\n' + \
           'grad(magSqr(rhoU)) leastSquares;' + '\n' + \
           'grad(rhoE) leastSquares;' + '\n' + \
           'grad(U) leastSquares;' + '\n' + \
           ' grad(T) leastSquares;' + '\n' + \
           ' } \n' + \
           '  \n' + \
           ' divSchemes \n' + \
           ' { \n' + \
           '     default         {}; \n'.format(param['divSchemes']) + \
           '  \n' + \
           '     div(tauMC)      Gauss linear; \n' + \
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
           '     interpolate(thermo:c) linear; \n' + \
           '     reconstruct(thermo:rho)    upwind; \n' + \
           '     reconstruct(rhoU) upwind;          \n' + \
           '    reconstruct(rhoE)   upwind; \n' + \
           ' } \n' + \
           '  \n' + \
           ' snGradSchemes \n' + \
           ' { \n' + \
           '     default         {}; \n'.format(param['snGradSchemes']) + \
           ' } \n' + \
           '  \n'
