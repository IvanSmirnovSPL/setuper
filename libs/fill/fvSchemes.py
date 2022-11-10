def fill_fvSchemes(params):
    return      'compressible' + '\n' + \
     '{' + '\n' + \
     r'fluxScheme {};'.format(params['compressible_fluxScheme']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'ddtSchemes' + '\n' + \
     '{' + '\n' + \
     r'default {};'.format(params['ddtSchemes_default']) + '\n' + \
     r'fluxIntegrator {};'.format(params['ddtSchemes_fluxIntegrator']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'gradSchemes' + '\n' + \
     '{' + '\n' + \
     r'default Gauss {};'.format(params['gradSchemes_default']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'divSchemes' + '\n' + \
     '{' + '\n' + \
     r'default {};'.format(params['divSchemes_default']) + '\n' + \
     r'    div(tauMC) Gauss {};'.format(params['divSchemes_div_tauMC_']) + '\n' + \
     r'    div((S&U)) Gauss {};'.format(params['divSchemes_div_SU_']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'laplacianSchemes' + '\n' + \
     '{' + '\n' + \
     r'default Gauss linear {};'.format(params['laplacianSchemes_default']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'interpolationSchemes' + '\n' + \
     '{' + '\n' + \
     r'default {};'.format(params['interpolationSchemes_default']) + '\n' + \
     r'scheme {};'.format(params['interpolationSchemes_scheme']) + '\n' + \
     '    ' + '\n' + \
     r'    reconstruct(thermo:rho) {};'.format(params['interpolationSchemes_reconstruct_thermorho_']) + '\n' + \
     r'    reconstruct(rhoU) {};'.format(params['interpolationSchemes_reconstruct_rhoU_']) + '\n' + \
     r'    reconstruct(rhoE) {};'.format(params['interpolationSchemes_reconstruct_rhoE_']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'snGradSchemes' + '\n' + \
     '{' + '\n' + \
     r'default {};'.format(params['snGradSchemes_default']) + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '// ************************************************************************* /' + '\n '
