system = \
    {
        'blockMeshDict':
            {

            },
        'controlDict':
            {
                'startFrom': 'latestTime',
                'startTime': '0',
                'stopAt': 'endTime',
                'endTime': '0.05',
                'deltaT': '1e-8',
                'writeControl': 'adjustable',
                'writeInterval': '0.001',
                'purgeWrite': '0',
                'writeFormat': 'ascii',
                'writePrecision': '6',
                'writeCompression': 'off',
                'timeFormat': 'general',
                'runTimeModifiable': 'yes',
                'adjustTimeStep': 'on',
                'maxCo': '5'

            },
        'decomposeParDict':
            {
                'numberOfSubdomains': '1'
            },
        'fvSchemes':
            {
                'Gllc': '0.5'
            },
        'fvSolution':
            {
                'cAlpha': 0,
                'nAlphaCorr': 2,
                'tolerance': '1e-6',
                'relTol': '0.1',
                'momentumPredictor': 'no',
                'nOuterCorrectors': '1',
                'nCorrectors': '3',
                'nNonOrthogonalCorrectors': '0',
                'U.*': '1',
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
                'internal_value': '100000',
                'boundary_types': ['in', 'out_with_value', 'symmetry', 'wall'],
                'boundary_name': {'out_with_value': 'fixedValue', 'wall': 'fixedFluxPressure'},
                'value': {'out_with_value': '$internalField', 'in_with_value': '$internalField'}
            },
        'U':
            {
                'internal_value': '(0 0 20)',
                'boundary_types': ['in_with_value', 'out_with_value', 'symmetry', 'wall'],
                'boundary_name': {'out_with_value': 'pressureInletOutletVelocity'},
                'value': {'in_with_value': '$internalField', 'out_with_value': '$internalField'}
            },
        'alpha.water':
            {

                'internal_value': '1',
                'boundary_types': ['in_with_value', 'out_with_value', 'symmetry', 'wall'],
                'boundary_name': {'wall': 'zeroGradient', 'out_with_value': 'inletOutlet'},
                'value': {'in_with_value': '$internalField', 'out_with_value': '$internalField'}
            }
    }

files_data = {'system': system, 'constant': constant, '0.orig': zero}


