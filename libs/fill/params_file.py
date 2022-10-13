def fill_params(params):
    return 'a {};'.format(params['a']) + '\n' + \
           'L {};'.format(params['L']) + '\n' + \
           'shift {};'.format(params['shift']) + '\n' + \
           'N {};'.format(params['N']) + '\n' + \
           '' + '\n' + \
           'U_left (0 0 0);' + '\n' + \
           'U_right (0 0 0);' + '\n' + \
           '' + '\n' + \
           'T_left {};'.format(params['T_left']) + '\n' + \
           'T_right {};'.format(params['T_right']) + '\n' + \
           '' + '\n' + \
           'p_left {};'.format(params['p_left']) + '\n' + \
           'p_right {};'.format(params['p_right']) + '\n' + \
           '' + '\n' + \
           'alpha_left 1e-1;' + '\n' + \
           'alpha_right 0.999;'
