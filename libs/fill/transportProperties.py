def fill_transportProperties(params):
    return '  '  + '\n' + \
 ' phases          (water vapour); '  + '\n' + \
 '  '  + '\n' + \
 ' phaseChangeTwoPhaseMixture SchnerrSauer; '  + '\n' + \
 '  '  + '\n' + \
 ' pSat            2300;   // Saturation pressure '  + '\n' + \
 '  '  + '\n' + \
 ' sigma           0.07; '  + '\n' + \
 '  '  + '\n' + \
 ' water '  + '\n' + \
 ' { '  + '\n' + \
 '     transportModel  Newtonian; '  + '\n' + \
 '     nu              9e-07; '  + '\n' + \
 '     rho             1000; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' vapour '  + '\n' + \
 ' { '  + '\n' + \
 '     transportModel  Newtonian; '  + '\n' + \
 '     nu              4.273e-04; '  + '\n' + \
 '     rho             0.02308; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' KunzCoeffs '  + '\n' + \
 ' { '  + '\n' + \
 '     UInf            U20.0; '  + '\n' + \
 '     tInf            0.005; // L = 0.1 m '  + '\n' + \
 '     Cc              C1000; '  + '\n' + \
 '     Cv              C1000; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' MerkleCoeffs '  + '\n' + \
 ' { '  + '\n' + \
 '     UInf            20.0; '  + '\n' + \
 '     tInf            0.005;  // L = 0.1 m '  + '\n' + \
 '     Cc              80; '  + '\n' + \
 '     Cv              1e-03; '  + '\n' + \
 ' } '  + '\n' + \
 '  '  + '\n' + \
 ' SchnerrSauerCoeffs '  + '\n' + \
 ' { '  + '\n' + \
 '     n               1.6e+13; '  + '\n' + \
 '     dNuc            2.0e-06; '  + '\n' + \
 '     Cc              1; '  + '\n' + \
 '     Cv              1; '  + '\n' + \
 ' } '