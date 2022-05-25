files_data = {
    'system':
        {
            'blockMeshDict': {'scale': 1},
            'controlDict': {'application': 'icoFoam',
                            'startFrom': 'startTime',
                            'startTime': 0,
                            'stopAt': 'endTime',
                            'endTime': 3,
                            'deltaT': 0.005,
                            'writeControl': 'timeStep',
                            'writeInterval': 20,
                            'purgeWrite': 0,
                            'writeFormat': 'ascii',
                            'writePrecision': 6,
                            'writeCompression': 'off',
                            'timeFormat': 'general',
                            'timePrecision': 6,
                            'runTimeModifiable': 'true',
                            },
            'decomposeParDict': {
                            'numberOfSubdomains': 9,
                            'method': 'hierarchical',
                            'coefs': {'n': '(3 3 1)'}

                                },
            'fvSchemes': {
                'ddtSchemes': {'default': 'Euler'},
                'gradSchemes': {'default': 'Gauss linear', 'grad(p)': 'Gauss linear'},
                'divSchemes': {'default': 'none', 'div(phi,U)': 'Gauss linear'},
                'laplacianSchemes': {'default': 'Gauss linear orthogonal'},
                'interpolationSchemes': {'default': 'linear'},
                'snGradSchemes': {'default': 'orthogonal'}
            }, 'fvSolution': {'solvers':{
            'p': {'solver': 'PCG', 'preconditioner': 'DIC', 'tolerance': 1e-6, 'relTol': 0.05},
            'pFinal': {'$p': '', 'relTol': 0},
            'U': {'solver': 'smoothSolver', 'smoother': 'symGaussSeidel', 'tolerance': 1e-5, 'relTol': 0}},
            'PISO': {'nCorrectors': 2, 'nNonOrthogonalCorrectors': 0, 'pRefCell': 0, 'pRefValue': 0}
        }, 'PDRblockMeshDict': {
            'scale': 0.1,
            'x': {'points': '(0 1)', 'nCells': '(20)', 'ratios': '(1)'},
            'y': {'points': '(0 1)', 'nCells': '(20)', 'ratios': '(1)'},
            'z': {'points': '(0 0.1)', 'nCells': '(1)', 'ratios': '(1)'},
            'boundary': ({
                'movingWall': {'type': 'wall', 'faces': '(3)'},
                'fixedWalls': {'type': 'wall', 'faces': '(0 1 2)'},
                'frontAndBack': {'type': 'empty', 'faces': '(4 5)'}},
            )
        }
        },
    'constant':
        {'transportProperties': {'nu': 0.01}},
    '0':
        {'p': {
         'dimensions': '[0 2 -2 0 0 0 0]',
         'internalField': 'uniform 0',
         'boundaryField': {'movingWall': {'type': 'zeroGradient'},
                           'fixedWalls': {'type': 'zeroGradient'},
                           'frontAndBack': {'type': 'empty'}}
        }, 'U': {
            'dimensions': ' [0 1 -1 0 0 0 0]',
            'internalField': 'uniform (0 0 0)',
            'boundaryField': {'movingWall': {'type': 'fixedValue', 'value': 'uniform (1 0 0)'},
                              'fixedWalls': {'type': 'noSlip'},
                              'frontAndBack': {'type': 'empty'}}
        }}
}
