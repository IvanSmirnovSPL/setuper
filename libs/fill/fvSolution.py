def fill_fvSolution(params):
    return 'solvers' + '\n' + \
           '{' + '\n' + \
           '    "alpha.water.*"' + '\n' + \
           '    {' + '\n' + \
           '        cAlpha          {};'.format(params['cAlpha']) + '\n' + \
           '        nAlphaCorr      {};'.format(params['nAlphaCorr']) + '\n' + \
           '        nAlphaSubCycles 1;' + '\n' + \
           ' ' + '\n' + \
           '        MULESCorr       yes;' + '\n' + \
           '        nLimiterIter    5;' + '\n' + \
           ' ' + '\n' + \
           '        solver          smoothSolver;' + '\n' + \
           '        smoother        symGaussSeidel;' + '\n' + \
           '        tolerance       {};'.format(params['tolerance']) + '\n' + \
           '        relTol          {};'.format(params['relTol']) + '\n' + \
           '        maxIter         10;' + '\n' + \
           '    };' + '\n' + \
           ' ' + '\n' + \
           '    "U.*" ' + '\n' + \
           '    {' + '\n' + \
           '        solver          smoothSolver;' + '\n' + \
           '        smoother        symGaussSeidel;' + '\n' + \
           '        tolerance       {};'.format(params['tolerance']) + '\n' + \
           '        relTol          {};'.format(params['relTol']) + '\n' + \
           '    };' + '\n' + \
           '  ' + '\n' + \
           '    p_rgh' + '\n' + \
           '    {' + '\n' + \
           '        solver          GAMG;' + '\n' + \
           '        tolerance       {};'.format(params['tolerance']) + '\n' + \
           '        relTol          {};'.format(params['relTol']) + '\n' + \
           '        smoother        DICGaussSeidel;' + '\n' + \
           '        maxIter         50;' + '\n' + \
           '    };' + '\n' + \
           ' ' + '\n' + \
           '    p_rghFinal' + '\n' + \
           '    {' + '\n' + \
           '        solver          PCG;' + '\n' + \
           '        preconditioner' + '\n' + \
           '        {' + '\n' + \
           '            preconditioner  GAMG;' + '\n' + \
           '            tolerance       {};'.format(params['tolerance']) + '\n' + \
           '            relTol          {};'.format(params['relTol']) + '\n' + \
           '            nVcycles        2;' + '\n' + \
           '            smoother        DICGaussSeidel;' + '\n' + \
           ' ' + '\n' + \
           '        };' + '\n' + \
           '        tolerance       {};'.format(params['tolerance']) + '\n' + \
           '        relTol          {};'.format(params['relTol']) + '\n' + \
           '        maxIter         50;' + '\n' + \
           '    };' + '\n' + \
           ' ' + '\n' + \
           '    "pcorr.*" ' + '\n' + \
           '    {' + '\n' + \
           '        $p_rgh;' + '\n' + \
           '        relTol          {};'.format(params['relTol']) + '\n' + \
           '    };' + '\n' + \
           ' ' + '\n' + \
           '    Phi' + '\n' + \
           '    {' + '\n' + \
           '        $p_rgh;' + '\n' + \
           '        relTol          {};'.format(params['relTol']) + '\n' + \
           '    };' + '\n' + \
           ' ' + '\n' + \
		'    "(k|kFinal|epsilon|omega|omegaFinal|nuTilda|phit)"\n'  + \
		'    {\n'  + \
		'        solver          PBiCGStab;\n'  + \
		'        preconditioner  DILU;\n'  + \
		'        tolerance       1e-8;\n'  + \
		'        relTol          0;\n'  + \
		'    }\n'  + \
		'\n'  + \
		'    f\n'  + \
		'    {\n'  + \
		'        solver          PBiCGStab;\n'  + \
		'        preconditioner  DIC;\n'  + \
		'        tolerance       1e-8;\n'  + \
		'        relTol          0;\n'  + \
		'    }\n'  + \
		'}\n'  + \
		'\n'  + \
		'potentialFlow\n'  + \
		'{\n'  + \
		'    nNonOrthogonalCorrectors   3;\n'  + \
		'}\n'  + \
		'\n'  + \
		'PIMPLE' + '\n' + \
           '{' + '\n' + \
           '    momentumPredictor           {};'.format(params['momentumPredictor']) + '\n' + \
           '    nOuterCorrectors            {};'.format(params['nOuterCorrectors']) + '\n' + \
           '    nCorrectors                 {};'.format(params['nCorrectors']) + '\n' + \
           '    nNonOrthogonalCorrectors    {};'.format(params['nNonOrthogonalCorrectors']) + '\n' + \
           '}' + '\n' + \
           ' ' + '\n' + \
           'relaxationFactors' + '\n' + \
           '{' + '\n' + \
           '    equations' + '\n' + \
           '    {' + '\n' + \
           '        "U.*"                   {};'.format(params['U.*']) + '\n' + \
           '    }' + '\n' + \
           '}'
'\n'  + \
'\n'  + \
'// ************************************************************************* //\n'
