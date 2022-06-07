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
    '        tolerance       1e-8;' + '\n' + \
    '        relTol          0;' + '\n' + \
    '        maxIter         10;' + '\n' + \
    '    };' + '\n' + \
    ' ' + '\n' + \
    '    "U.*" ' + '\n' + \
    '    {' + '\n' + \
    '        solver          smoothSolver;' + '\n' + \
    '        smoother        symGaussSeidel;' + '\n' + \
    '        tolerance       1e-6;' + '\n' + \
    '        relTol          0;' + '\n' + \
    '    };' + '\n' + \
    '  ' + '\n' + \
    '    p_rgh' + '\n' + \
    '    {' + '\n' + \
    '        solver          GAMG;' + '\n' + \
    '        tolerance       1e-8;' + '\n' + \
    '        relTol          0.1;' + '\n' + \
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
    '            tolerance       1e-6;' + '\n' + \
    '            relTol          0;' + '\n' + \
    '            nVcycles        2;' + '\n' + \
    '            smoother        DICGaussSeidel;' + '\n' + \
    ' ' + '\n' + \
    '        };' + '\n' + \
    '        tolerance       1e-7;' + '\n' + \
    '        relTol          0;' + '\n' + \
    '        maxIter         50;' + '\n' + \
    '    };' + '\n' + \
    ' ' + '\n' + \
    '    "pcorr.*" ' + '\n' + \
    '    {' + '\n' + \
    '        $p_rgh;' + '\n' + \
    '        relTol          0;' + '\n' + \
    '    };' + '\n' + \
    ' ' + '\n' + \
    '    Phi' + '\n' + \
    '    {' + '\n' + \
    '        $p_rgh;' + '\n' + \
    '        relTol          0;' + '\n' + \
    '    };' + '\n' + \
    '}' + '\n' + \
    ' ' + '\n' + \
    'potentialFlow' + '\n' + \
    '{' + '\n' + \
    '    nNonOrthogonalCorrectors   3;' + '\n' + \
    '}' + '\n' + \
    ' ' + '\n' + \
    'PIMPLE' + '\n' + \
    '{' + '\n' + \
    '    momentumPredictor           no;' + '\n' + \
    '    nOuterCorrectors            1;' + '\n' + \
    '    nCorrectors                 3;' + '\n' + \
    '    nNonOrthogonalCorrectors    0;' + '\n' + \
    '}' + '\n' + \
    ' ' + '\n' + \
    'relaxationFactors' + '\n' + \
    '{' + '\n' + \
    '    equations' + '\n' + \
    '    {' + '\n' + \
    '        "U.*"                   1;' + '\n' + \
    '    }' + '\n' + \
    '}'
