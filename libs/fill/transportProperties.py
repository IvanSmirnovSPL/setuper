def fill_transportProperties(params):
    return '  ' + '\n' + \
           ' phases          (water vapour); ' + '\n' + \
           '  ' + '\n' + \
           ' phaseChangeTwoPhaseMixture {}; '.format(params['phaseChangeTwoPhaseMixture']) + '\n' + \
           '  ' + '\n' + \
           ' pSat            {};   // Saturation pressure '.format(params['pSat']) + '\n' + \
           '  ' + '\n' + \
           ' sigma           {}; '.format(params['sigma']) + '\n' + \
           '  ' + '\n' + \
           ' water ' + '\n' + \
           ' { ' + '\n' + \
           '     transportModel  {}; '.format(params['transportModel']) + '\n' + \
           '     nu              {}; '.format(params['nu_water']) + '\n' + \
           '     rho             {}; '.format(params['rho_water']) + '\n' + \
           ' } ' + '\n' + \
           '  ' + '\n' + \
           ' vapour ' + '\n' + \
           ' { ' + '\n' + \
           '     transportModel  {}; '.format(params['transportModel']) + '\n' + \
           '     nu              {}; '.format(params['nu_vapour']) + '\n' + \
           '     rho             {}; '.format(params['rho_vapour']) + '\n' + \
           ' } ' + '\n' + \
           '  ' + '\n' + \
           ' KunzCoeffs ' + '\n' + \
           ' { ' + '\n' + \
           '     UInf            {}; '.format(params['UInf_Kunz']) + '\n' + \
           '     tInf            {}; // L = 0.1 m '.format(params['tInf_Kunz']) + '\n' + \
           '     Cc              {}; '.format(params['Cc_Kunz']) + '\n' + \
           '     Cv              {}; '.format(params['Cv_Kunz']) + '\n' + \
           ' } ' + '\n' + \
           '  ' + '\n' + \
           ' MerkleCoeffs ' + '\n' + \
           ' { ' + '\n' + \
           '     UInf            {}; '.format(params['Cv_Merkle']) + '\n' + \
           '     tInf            {};  // L = 0.1 m '.format(params['Cv_Merkle']) + '\n' + \
           '     Cc              {}; '.format(params['Cv_Merkle']) + '\n' + \
           '     Cv              {}; '.format(params['Cv_Merkle']) + '\n' + \
           ' } ' + '\n' + \
           '  ' + '\n' + \
           ' SchnerrSauerCoeffs ' + '\n' + \
           ' { ' + '\n' + \
           '     n               {}; '.format(params['n']) + '\n' + \
           '     dNuc            {}; '.format(params['dNuc']) + '\n' + \
           '     Cc              {}; '.format(params['Cc_SchnerrSauer']) + '\n' + \
           '     Cv              {}; '.format(params['Cv_SchnerrSauer']) + '\n' + \
           ' } '
