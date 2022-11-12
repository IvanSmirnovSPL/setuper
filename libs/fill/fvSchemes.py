def fill_fvSchemes(params):
    return  r'' + '\n' + \
     r'compressible' + '\n' + \
     r'{' + '\n' + \
     r'    fluxScheme       AUSMPlusUp;' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'ddtSchemes' + '\n' + \
     r'{' + '\n' + \
     r'    default          Euler;' + '\n' + \
     r'    fluxIntegrator   RK2SSP;' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'gradSchemes' + '\n' + \
     r'{' + '\n' + \
     r'    default         none;//cellLimited<Venkatakrishnan> leastSquares 1.0;' + '\n' + \
     r'    a cellLimited<Venkatakrishnan> leastSquares 1.0;' + '\n' + \
     r'    grad(thermo:rho) leastSquares;' + '\n' + \
     r'    grad(magSqr(rhoU)) leastSquares;' + '\n' + \
     r'    grad(rhoE) leastSquares;' + '\n' + \
     r'    grad(U) leastSquares;' + '\n' + \
     r'    grad(T) leastSquares;' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'divSchemes' + '\n' + \
     r'{' + '\n' + \
     r'    default         none;' + '\n' + \
     r'' + '\n' + \
     r'    div(tauMC)      Gauss linear;//WENOUpwindFit 3 0;' + '\n' + \
     r'    div((S&U))      Gauss linear;//WENOUpwindFit 3 0;' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'laplacianSchemes' + '\n' + \
     r'{' + '\n' + \
     r'    default         Gauss linear corrected;' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'interpolationSchemes' + '\n' + \
     r'{' + '\n' + \
     r'    default         none;' + '\n' + \
     r'    flux(U)         linear;' + '\n' + \
     r'    interpolate(thermo:c) linear;' + '\n' + \
     r'    ' + '\n' + \
     r'    scheme upwind;//vanLeer;//linearUpwind a;//vanLeer;//Minmod; //vanLeer;' + '\n' + \
     r'    ' + '\n' + \
     r'    reconstruct(thermo:rho) $scheme;' + '\n' + \
     r'    reconstruct(rhoU) $scheme;' + '\n' + \
     r'    reconstruct(rhoE) $scheme;' + '\n' + \
     r'' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'snGradSchemes' + '\n' + \
     r'{' + '\n' + \
     r'    default         corrected;' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'// ************************************************************************* //' + '\n '
