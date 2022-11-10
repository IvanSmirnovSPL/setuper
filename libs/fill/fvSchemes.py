def fill_fvSchemes(params):
    return      r'FoamFile' + '\n' + \
     r'{' + '\n' + \
     r'    version     2.0;' + '\n' + \
     r'    format      ascii;' + '\n' + \
     r'    class       dictionary;' + '\n' + \
     r'    location    "system";' + '\n' + \
     r'    object      fvSchemes;' + '\n' + \
     r'}' + '\n' + \
     r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
     'compressibl' + '\n' + \
     '' + '\n' + \
     r'fluxScheme {};'.format(params['compressible_fluxScheme']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'ddtScheme' + '\n' + \
     '' + '\n' + \
     r'default {};'.format(params['ddtSchemes_default']) + '\n' + \
     r'fluxIntegrator {};'.format(params['ddtSchemes_fluxIntegrator']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'gradScheme' + '\n' + \
     '' + '\n' + \
     r'default Gauss {};'.format(params['gradSchemes_default']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'divScheme' + '\n' + \
     '' + '\n' + \
     r'default {};'.format(params['divSchemes_default']) + '\n' + \
     r'    div({});'.format(params['divSchemes_div_tauMC_']) + '\n' + \
     r'    div(({});'.format(params['divSchemes_div_SU_']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'laplacianScheme' + '\n' + \
     '' + '\n' + \
     r'default Gauss linear {};'.format(params['laplacianSchemes_default']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'interpolationScheme' + '\n' + \
     '' + '\n' + \
     r'default {};'.format(params['interpolationSchemes_default']) + '\n' + \
     r'scheme {};'.format(params['interpolationSchemes_scheme']) + '\n' + \
     '   ' + '\n' + \
     r'    reconstruct({});'.format(params['interpolationSchemes_reconstruct_thermorho_']) + '\n' + \
     r'    reconstruct({});'.format(params['interpolationSchemes_reconstruct_rhoU_']) + '\n' + \
     r'    reconstruct({});'.format(params['interpolationSchemes_reconstruct_rhoE_']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'snGradScheme' + '\n' + \
     '' + '\n' + \
     r'default {};'.format(params['snGradSchemes_default']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '// ************************************************************************* /' + '\n '
