files_data = {
    'system':
        {
            'blockMeshDict': {'scale': '0.001',

                              'vertices':
                                  (
                                      '(-15 -15 -15)',
                                      '(15 -15 -15)',
                                      '(15  15 -15)',
                                      '(-15  15 -15)',
                                      '(-15 -15 100)',
                                      '(15 -15 100)',
                                      '(15  15 100)',
                                      '(-15  15 100)'
                                  ),

                              'blocks':
                                  (
                                      'hex (0 1 2 3 4 5 6 7) (15 15 50) simpleGrading (1 1 1)',
                                  ),

                              'boundary':
                                  ({
                                       'inlet':
                                           {
                                               'type': 'patch',
                                               'faces':
                                                   (
                                                       '(0 3 2 1)',
                                                   )
                                           },
                                       'outlet':
                                           {
                                               'type': 'patch',
                                               'faces':
                                                   (
                                                       '(4 5 6 7)',
                                                   )
                                           },
                                       'walls':
                                           {
                                               'type': 'symmetry',
                                               'faces':
                                                   (
                                                       '(0 4 7 3)',
                                                       '(2 6 5 1)',
                                                       '(1 5 4 0)',
                                                       '(3 7 6 2)'
                                                   )
                                           }
                                   },)
                              },
            'controlDict': {'application': 'interPhaseChangeFoam',

                            'startFrom': 'latestTime',

                            'startTime': 0,

                            'stopAt': 'endTime',

                            'endTime': 0.05,

                            'deltaT': 1e-8,

                            'writeControl': 'adjustable',

                            'writeInterval': 0.001,

                            'purgeWrite': 0,

                            'writeFormat': 'ascii',

                            'writePrecision': 6,

                            'writeCompression': 'off',

                            'timeFormat': 'general',

                            'runTimeModifiable': 'yes',

                            'adjustTimeStep': 'on',

                            'maxCo': 5},
            'decomposeParDict': {
                'numberOfSubdomains': 4,

                'method': 'simple',

                'coeffs':
                    {
                        'n': '(2 2 1)'
                    }

            },
            'fvSchemes': {
                'ddtSchemes':
                    {
                        'default': 'Euler'
                    },

                'interpolationSchemes':
                    {
                        'default': 'linear'
                    },

                'divSchemes':
                    {
                        'default': 'none',
                        'div(rhoPhi,U)': 'Gauss linearUpwind grad(U)',
                        'div(phi,omega)': 'Gauss linearUpwind grad(omega)',
                        'div(phi,k)': 'Gauss linearUpwind grad(k)',
                        'div(phi,alpha)': 'Gauss vanLeer',
                        'div(phirb,alpha)': 'Gauss linear',
                        'div(((rho*nuEff)*dev2(T(grad(U)))))': 'Gauss linear'
                    },

                'gradSchemes':
                    {
                        'default': 'Gauss linear'
                    },

                'laplacianSchemes':
                    {
                        'default': 'Gauss linear limited corrected 0.5'
                    },

                'snGradSchemes':
                    {
                        'default': 'limited corrected 0.5'
                    }

            }, 'fvSolution': {'solvers': {
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
        {'transportProperties': {'phases': '(water vapour)',
                                 'phaseChangeTwoPhaseMixture': 'SchnerrSauer',
                                 'pSat': 2300,
                                 'sigma': 0.07,
                                 'water': {'transportModel': 'Newtonian',
                                           'nu': 9e-07,
                                           'rho': 1000},
                                 'vapour': {'transportModel': 'Newtonian',
                                            'nu': 4.273e-04,
                                            'rho': 0.02308},
                                 'KunzCoeffs': {'UInf': 'U20.0',
                                                'tInf': 0.005,
                                                'Cc': 'C1000',
                                                'Cv': 'C1000'
                                                },
                                 'MerkleCoeffs': {'UInf': 20.0,
                                                  'tInf': 0.005,
                                                  'Cc': 80,
                                                  'Cv': 1e-03
                                                  },
                                 'SchnerrSauerCoeffs': {
                                     'n': 1.6e13,
                                     'dNuc': 2.0e-06,
                                     'Cc': 1,
                                     'Cv': 1
                                 }
                                 },
         'turbulenceProperties': {'simulationType': 'laminar'},
         'g': {'dimensions': '[0 1 -2 0 0 0 0]',
               'value': '(0 -9.81 0)'}},
    '0.orig':
        {'p_rgh': {'dimensions': '[1 -1 -2 0 0]',

                   'internalField': 'uniform 100000',

                   'boundaryField':
                       {
                           'inlet':
                               {
                                   'type': 'zeroGradient'
                               },

                           'outlet':
                               {
                                   'type': 'fixedValue',
                                   'value': '$internalField'
                               },

                           'walls':
                               {
                                   'type': 'symmetry'
                               },

                           'bullet':
                               {
                                   'type': 'fixedFluxPressure'
                               }
                       }
                   }, 'U': {'dimensions': '[0 1 -1 0 0]',

                            'internalField': 'uniform (0 0 20)',

                            'boundaryField':
                                {
                                    'inlet':
                                        {
                                            'type'            'fixedValue',
                                            'value'           '$internalField',
                                        },

                                    'outlet':
                                        {
                                            'type'            'pressureInletOutletVelocity',
                                            'value'           '$internalField',
                                        },

                                    'walls':
                                        {
                                            'type': 'symmetry'
                                        },

                                    'bullet':
                                        {
                                            'type': 'noSlip'
                                        }
                                }
                            },
         'Phi': {'dimensions': '[0 2 -1 0 0]',

                 'internalField': 'uniform 0',

                 'boundaryField':
                     {
                         'inlet':
                             {
                                 'type': 'zeroGradient'
                             },

                         'outlet':
                             {
                                 'type': 'fixedValue',
                                 'value': '$internalField'
                             },

                         'walls':
                             {
                                 'type': 'symmetry'
                             },

                         'bullet':
                             {
                                 'type': 'zeroGradient'
                             }
                     }},
         'alpha.water': {'dimensions': '[0 0 0 0 0]',

                         'internalField': 'uniform 1',

                         'boundaryField':
                             {
                                 'inlet':
                                     {
                                         'type': 'fixedValue',
                                         'value': '$internalField'
                                     },

                                 'outlet':
                                     {
                                         'type': 'inletOutlet',
                                         'inletValue': '$internalField'
                                     },

                                 'walls':
                                     {
                                         'type': 'symmetry'
                                     },

                                 'bullet':
                                     {
                                         'type': 'zeroGradient'
                                     }
                             }}
         }
}
