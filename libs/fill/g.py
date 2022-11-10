def fill_g(params):
    return      r'FoamFile' + '\n' + \
     r'{' + '\n' + \
     r'    version     2.0;' + '\n' + \
     r'    format      ascii;' + '\n' + \
     r'    class       uniformDimensionedVectorField;' + '\n' + \
     r'    location    "constant";' + '\n' + \
     r'    object      g;' + '\n' + \
     r'}' + '\n' + \
     r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
     '' + '\n' + \
     'dimensions      [0 1 -2 0 0 0 0]' + '\n' + \
     r'value           ({});'.format(params['value']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '// ************************************************************************* /' + '\n '
