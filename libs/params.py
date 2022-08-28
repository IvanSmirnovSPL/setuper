system = \
    {
        'blockMeshDict':
            {

            },
        'controlDict':
            {
                'libs': 0,
                'application': 0,
                'startFrom': 0,
                'startTime': 0,
                'stopAt': 0,
                'endTime': 0,
                'deltaT': 0,
                'writeControl': 0,
                'writeInterval': 0,
                'purgeWrite': 0,
                'writeFormat': 0,
                'writePrecision': 0,
                'writeCompression': 0,
                'timeFormat': 0,
                'timePrecision': 0,
                'runTimeModifiable': 0,
                'adjustTimeStep': 0,
                'maxCo': 0,
                'maxDeltaT': 0,
            },
        'decomposeParDict':
            {
                'numberOfSubdomains': '1'
            },
        'fvSchemes':
            {
                'fluxScheme': 0,
                'ddtSchemes': 0,
                'fluxIntegrator': 0,
                'gradSchemes': 0,
                'divSchemes': 0,
                'div(tauMC)': 0,
                'laplacianSchemes': 0,
                'interpolationSchemes': 0,
                'reconstruct_U': 0,
                'reconstruct_p': 0,
                'reconstruct_thermo': 0,
                'snGradSchemes': 0,
            },
        'fvSolution':
            {
                'solver': 0,
                'U_solver': 0,
                'smoother': 0,
                'nSweeps': 0,
                'tolerance': 0,
                'relTol': 0,
                '$U;': 0,
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
        'thermophysicalProperties':
            {
                'phases': 0,
                'Tmin': 0,
                'Tmax': 0,
                'relTol': 0,
                'maxIter': 0,
                'logPSatFile': 0,
                'TSatFile': 0,
                'rho1SatFile': 0,
                'rho2SatFile': 0,
                'rho1SatDerFile': 0,
                'rho2SatDerFile': 0,
                'gvFile': 0,
                'glFile': 0,
                'TstepFile': 0,
            },
        'g':
            {
                'dimensions_g': '[0 1 -2 0 0 0 0]',
                'g': -9.81
            }
    }

zero = \
    {
        'p':
            {
                'internal_value': '100000',
                'boundary_types': ['empty', 'out'],
            },
        'T':
            {
                'internal_value': '100000',
                'boundary_types': ['empty', 'out'],
            },
        'U':
            {
                'internal_value': '(0 0 20)',
                'boundary_types': ['empty', 'out'],
            },
        'alpha.water':
            {

                'internal_value': '1',
                'boundary_types': ['empty', 'out'],
            }
    }

files_data = {'system': system, 'constant': constant, '0.orig': zero}
