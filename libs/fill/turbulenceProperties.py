def fill_turbulenceProperties(params):
    return      r'FoamFile' + '\n' + \
     r'{' + '\n' + \
     r'    version     2.0;' + '\n' + \
     r'    format      ascii;' + '\n' + \
     r'    class       dictionary;' + '\n' + \
     r'    object      turbulenceProperties;' + '\n' + \
     r'}' + '\n' + \
     r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
     '' + '\n' + \
     r'simulationType {};'.format(params['simulationType']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '// ************************************************************************* /' + '\n '
