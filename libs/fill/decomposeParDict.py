def fill_decomposeParDict(params):
    return      '' + '\n' + \
     r'numberOfSubdomains {};'.format(params['numberOfSubdomains']) + '\n' + \
     r'method {};'.format(params['method']) + '\n'
