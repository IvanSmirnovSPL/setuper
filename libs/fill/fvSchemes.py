def fill_fvSchemes(params):
    return  '  '  + '\n' + \
 ' ddtSchemes '  + '\n' + \
 ' { '  + '\n' + \
 '     default             Euler; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' interpolationSchemes '  + '\n' + \
 ' { '  + '\n' + \
 '     default             linear; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' divSchemes '  + '\n' + \
 ' { '  + '\n' + \
 '     default             none; '  + '\n' + \
 '     div(rhoPhi,U)       Gauss linearUpwind grad(U); '  + '\n' + \
 '     div(phi,omega)      Gauss linearUpwind grad(omega); '  + '\n' + \
 '     div(phi,k)          Gauss linearUpwind grad(k); '  + '\n' + \
 '     div(phi,alpha)      Gauss vanLeer; '  + '\n' + \
 '     div(phirb,alpha)    Gauss linear; '  + '\n' + \
 '     div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' gradSchemes '  + '\n' + \
 ' { '  + '\n' + \
 '     default             Gauss linear; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' laplacianSchemes '  + '\n' + \
 ' { '  + '\n' + \
 '     default             Gauss linear limited corrected 0.5; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' snGradSchemes '  + '\n' + \
 ' { '  + '\n' + \
 '     default             limited corrected 0.5; '  + '\n' + \
 ' } '
