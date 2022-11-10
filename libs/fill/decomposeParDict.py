def fill_decomposeParDict(params):
    return      r'FoamFile' + '\n' + \
     r'{' + '\n' + \
     r'	version 2.0;' + '\n' + \
     r'	format ascii;' + '\n' + \
     r'	class dictionary;' + '\n' + \
     r'	location system;' + '\n' + \
     r'	object decomposeParDict;' + '\n' + \
     r'}' + '\n' + \
     r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
     '' + '\n' + \
     r'numberOfSubdomains {};'.format(params['numberOfSubdomains']) + '\n' + \
     r'method {};'.format(params['method']) + '\n'
