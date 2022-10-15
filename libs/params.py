system = \
    {
        'controlDict':
            {
                'libs': "libWENOEXT.so",
                'application': 'FAKTFoam',
                'startFrom': 'startTime',
                'startTime': '0',
                'stopAt': 'endTime',
                'endTime': '1e-3',
                'deltaT': '1e-07',
                'writeControl': 'adjustable',
                'writeInterval': '1e-5',
                'purgeWrite': '0',
                'writeFormat': 'ascii',
                'writePrecision': '6',
                'writeCompression': 'off',
                'timeFormat': 'general',
                'timePrecision': '6',
                'runTimeModifiable': 'true',
                'adjustTimeStep': 'yes',
                'maxCo': '0.1',
                'maxDeltaT': '1',
            },
        'decomposeParDict':
            {
                'numberOfSubdomains': '1'
            },
        'fvSchemes':
            {
                'fluxScheme': 'AUSMPlusUp',
                'ddtSchemes': 'Euler',
                'fluxIntegrator': 'RK45',
                'gradSchemes': 'linear',
                'divSchemes': 'none',
                'div_tauMC': 'WENOUpwindFit 3 0',
                'laplacianSchemes': 'linear corrected',
                'interpolationSchemes': 'linear',
                'reconstruct_U': 'upwind',
                'reconstruct_p': 'upwind',
                'reconstruct_thermo': 'upwind',
                'snGradSchemes': 'corrected',
            },
        'fvSolution':
            {
                'solver': 'diagonal',
                'U_solver': 'smoothSolver',
                'smoother': 'GaussSeidel',
                'nSweeps': '2',
                'tolerance': '1e-9',
                'relTol': '0.01',
                'U': '$U',
            },
        'params':
            {
                'a': '0.1',
                'L': '5.0',
                'N': '1000',
                'shift': '0.0',
                'p_left': '1.1e7',
                'p_right': '8.9e6',
                'T_left': '584.2360251538847',
                'T_right': '576.5818015076865'
            },
        'setFieldsDict': {}





    }

constant = \
    {
        'turbulenceProperties':
            {
                'simulationType': 'laminar',
            },
        'thermophysicalProperties':
            {
                'phases': 'vapour liquid',
                'Tmin': '0.001',
                'Tmax': '1000000',
                'relTol': '1e-5',
                'maxIter': '1000',
                'logPSatFile': 'logPSat.dat',
                'TSatFile': 'TSat.dat',
                'rho1SatFile': 'rhovSat.dat',
                'rho2SatFile': 'rholSat.dat',
                'rho1SatDerFile': 'rhovSatDer.dat',
                'rho2SatDerFile': 'rholSatDer.dat',
                'gvFile': 'gv.dat',
                'glFile': 'gl.dat',
                'TstepFile': 'Tstep.dat',
            },
        'g':
            {
                'g': ' 0 9.81 0',
                'dimensions_g' : '[0 1 -2 0 0 0 0]',
            },
    }

zero = \
    {
        'p':
            {
                'internal_value': '0',
                'value': {'out_with_value': 'uniform $p_right', 'in_with_value': 'uniform $p_left'},
                'boundary_types': ['empty', 'out_with_value', 'in_with_value'],
            },
        'T':
            {
                'internal_value': '1',
                'value': {'out_with_value': 'uniform $T_right', 'in_with_value': 'uniform $T_left'},
                'boundary_types': ['empty', 'out_with_value', 'in_with_value'],
            },
        'U':
            {
                'internal_value': '(0 0 0)',
                'value': {'out_with_value': 'uniform (0 0 0)', 'in_with_value': 'uniform (0 0 0)'},
                'boundary_types': ['empty', 'out_with_value', 'in_with_value'],
            },
        'alpha.vapour':
            {

                'internal_value': '1.0',
                'boundary_types': ['empty', 'out_with_value', 'in_with_value'],
            }
    }

files_data = {'system': system, 'constant': constant, '0.orig': zero}
