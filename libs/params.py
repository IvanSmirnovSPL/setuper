system = \
    {
        'blockMeshDict':
            {

            },
        'controlDict':
            {

            },
        'decomposeParDict':
            {

            },
        'fvSchemes':
            {

            },
        'fvSolution':
            {
                'cAlpha': 0,
                'nAlphaCorr': 2
            },
        'snappyHexMeshDict':
            {

            }

    }

constant = \
    {
        'transportProperties':
            {
                'phaseChangeTwoPhaseMixture': 'SchnerrSauer',
                'pSat': 2300,
                'sigma': 0.07,
                'nu_water': 9e-07,
                'rho_water': 1000,
                'transportModel': 'Newtonian',
                'nu_vapour': 4.273e-04,
                'rho_vapour': 0.02308,
                'UInf_Kunz': 'U20.0',
                'tInf_Kunz': 0.005,
                'Cc_Kunz': 'C1000',
                'Cv_Kunz': 'C1000',
                'UInf_Merkle': 20.0,
                'tInf_Merkle': 0.005,
                'Cc_Merkle': 80,
                'Cv_Merkle': 1e-03,
                'n': 1.6e13,
                'dNuc': 2.0e-06,
                'Cc_SchnerrSauer': 1,
                'Cv_SchnerrSauer': 1
            },
        'turbulenceProperties':
            {
                'simulationType': 'laminar'
            },
        'g':
            {
                'dimensions_g': '[0 1 -2 0 0 0 0]',
                'g': -9.81
            }
    }

zero = \
    {
        'p_rgh':
            {
                'dimensions_p_rgh': '[1 -1 -2 0 0]',
                'internalField_p_rgh': 'uniform 100000',
                'type_inlet_p_rgh': 'zeroGradient',
                'type_outlet_p_rgh': 'fixedValue',
                'value_outlet_p_rgh': '$internalField',
                'type_walls_p_rgh': 'symmetry',
                'type_bullet_p_rgh': 'fixedFluxPressure'
            },
        'U':
            {
                'dimensions_U': '[0 1 -1 0 0]',
                'internalField_U': 'uniform (0 0 20)',
                'type_inlet_U': 'fixedValue',
                'value_inlet_U': '$internalField',
                'type_outlet_U': 'pressureInletOutletVelocity',
                'value_outlet_U': '$internalField',
                'type_walls_U': 'symmetry',
                'type_bullet_U': 'noSlip',
            },
        'Phi':
            {
                'dimensions_Phi': '[0 2 -1 0 0]',
                'internalField_Phi': 'uniform 0',
                'type_inlet_Phi': 'zeroGradient',
                'type_outlet_Phi': 'fixedValue',
                'value_outlet_Phi': '$internalField',
                'type_walls_Phi': 'symmetry',
                'type_bullet_Phi': 'zeroGradient'
            },
        'alpha.water':
            {
                 'dimensions_alpha': '[0 0 0 0 0]',
                 'internalField_alpha': 'uniform 1',
                 'type_inlet_alpha': 'fixedValue',
                 'value_inlet_alpha': '$internalField',
                 'type_outlet_alpha': 'inletOutlet',
                 'inletValue_outlet_alpha': '$internalField',
                 'type_walls_alpha': 'symmetry',
                 'type_bullet_alpha': 'zeroGradient'
            }
    }

files_data = {'system': system, 'constant': constant, '0.orig': zero}

'''files_data = {
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

            }, 'fvSolution': {'cAlpha': 0, 'nAlphaCorr': 2}, 'snappyHexMeshDict': {}
        },

    'constant':
        {'transportProperties': {
            'phaseChangeTwoPhaseMixture': 'SchnerrSauer',
            'pSat': 2300,
            'sigma': 0.07,
            'nu_water': 9e-07,
            'rho_water': 1000,
            'transportModel': 'Newtonian',
            'nu_vapour': 4.273e-04,
            'rho_vapour': 0.02308,
            'UInf_Kunz': 'U20.0',
            'tInf_Kunz': 0.005,
            'Cc_Kunz': 'C1000',
            'Cv_Kunz': 'C1000',
            'UInf_Merkle': 20.0,
            'tInf_Merkle': 0.005,
            'Cc_Merkle': 80,
            'Cv_Merkle': 1e-03,
            'n': 1.6e13,
            'dNuc': 2.0e-06,
            'Cc_SchnerrSauer': 1,
            'Cv_SchnerrSauer': 1
        },
            'turbulenceProperties': {'simulationType': 'laminar'},
            'g': {'dimensions': '[0 1 -2 0 0 0 0]',
                  'g': '(0 -9.81 0)'}},

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
'''