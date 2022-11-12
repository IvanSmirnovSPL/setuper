def fill_fvSolution(params):
    return     r'' + '\n' + \
     r'solvers' + '\n' + \
     r'{' + '\n' + \
     r'    E' + '\n' + \
     r'    {' + '\n' + \
     r'        solver          a;' + '\n' + \
     r'        tolerance       1e-06;' + '\n' + \
     r'        relTol          0.1;' + '\n' + \
     r'        smoother        GaussSeidel;' + '\n' + \
     r'    }' + '\n' + \
     r'' + '\n' + \
     r'    "(U|k|epsilon|omega|f|v2)"' + '\n' + \
     r'    {' + '\n' + \
     r'        solver          smoothSolver;' + '\n' + \
     r'        smoother        symGaussSeidel;' + '\n' + \
     r'        tolerance       1e-05;' + '\n' + \
     r'        relTol          0.1;' + '\n' + \
     r'    }' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'SIMPLE' + '\n' + \
     r'{' + '\n' + \
     r'    nNonOrthogonalCorrectors 0;' + '\n' + \
     r'    consistent      yes;' + '\n' + \
     r'' + '\n' + \
     r'    residualControl' + '\n' + \
     r'    {' + '\n' + \
     r'        p               1e-2;' + '\n' + \
     r'        U               1e-3;' + '\n' + \
     r'        "(k|epsilon|omega|f|v2)" 1e-3;' + '\n' + \
     r'    }' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'relaxationFactors' + '\n' + \
     r'{' + '\n' + \
     r'    equations' + '\n' + \
     r'    {' + '\n' + \
     r'        U               0.9; // 0.9 is more stable but 0.95 more convergent' + '\n' + \
     r'        ".*"            0.9; // 0.9 is more stable but 0.95 more convergent' + '\n' + \
     r'    }' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'' + '\n' + \
     r'// ************************************************************************* //' + '\n '
