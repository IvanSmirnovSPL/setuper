def fill_fvSolution(params):
    return     '' + '\n' + \
     'solvers' + '\n' + \
     '{' + '\n' + \
     '    E' + '\n' + \
     '    {' + '\n' + \
     r'solver {};'.format(params['E_solver']) + '\n' + \
     r'preconditioner {};'.format(params['E_preconditioner']) + '\n' + \
     r'tolerance {};'.format(params['E_tolerance']) + '\n' + \
     r'relTol {};'.format(params['E_relTol']) + '\n' + \
     '    }' + '\n' + \
     '    U' + '\n' + \
     '    {' + '\n' + \
     r'solver {};'.format(params['U_solver']) + '\n' + \
     r'preconditioner {};'.format(params['U_preconditioner']) + '\n' + \
     r'tolerance {};'.format(params['U_tolerance']) + '\n' + \
     r'relTol {};'.format(params['U_relTol']) + '\n' + \
     '    }' + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'SIMPLE' + '\n' + \
     '{' + '\n' + \
     r'nNonOrthogonalCorrectors {};'.format(params['SIMPLE_nNonOrthogonalCorrectors']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '// ************************************************************************* /' + '\n '
