def fill_fvSolution(param):
    return '  \n' + \
           ' solvers \n' + \
           ' { \n' + \
           '      "(thermo:rho|rhoU|rhoE)" \n' + \
           '     { \n' + \
           '         solver          {}; \n'.format(param['solver']) + \
           '     } \n' + \
           '  \n' + \
           '     U \n' + \
           '     { \n' + \
           '         solver          {}; \n'.format(param['U_solver']) + \
           '         smoother        {}; \n'.format(param['smoother']) + \
           '         nSweeps         {}; \n'.format(param['nSweeps']) + \
           '         tolerance       {}; \n'.format(param['tolerance']) + \
           '         relTol          {}; \n'.format(param['relTol']) + \
           '     } \n' + \
           '  \n' + \
           '     h \n' + \
           '     { \n' + \
           '         {}; \n'.format(param['$U;']) + \
           '         tolerance       {}; \n'.format(param['tolerance']) + \
           '         relTol          {}; \n'.format(param['relTol']) + \
           '     } \n' + \
           ' } \n' + \
           '  \n' + \
           '  \n'
