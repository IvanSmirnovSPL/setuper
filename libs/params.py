system = \
    {
        'controlDict':
            {
                'application': 'laplacianMesh',
                'startFrom': 'startTime',
                'startTime': '0',
                'stopAt': 'endTime',
                'endTime': '300',
                'deltaT': '1e-8',
                'writeControl': 'timeStep',
                'writeInterval': '10',
                'purgeWrite': '0',
                'writeFormat': 'ascii',
                'writePrecision': '6',
                'writeCompression': 'off',
                'timeFormat': 'general',
                'timePrecision': '6',
                'runTimeModifiable': 'true',
                'adjustTimeStep': 'yes',
                'maxCo': '0.5',
                'maxDeltaT': '1',
            },
        'fvSchemes':
            {
                'compressible_fluxScheme': 'AUSMPlusUp',
                'ddtSchemes_default': 'Euler',
                'ddtSchemes_fluxIntegrator': 'Euler',
                'gradSchemes_default': 'linear',
                'divSchemes_default': 'none',
                'divSchemes_div_tauMC_': 'linear',
                'divSchemes_div_SU_': 'linear',
                'laplacianSchemes_default': 'corrected',
                'interpolationSchemes_default': 'linear',
                'interpolationSchemes_scheme': 'upwind',
                'interpolationSchemes_reconstruct_thermorho_': '$scheme',
                'interpolationSchemes_reconstruct_rhoU_': '$scheme',
                'interpolationSchemes_reconstruct_rhoE_': '$scheme',
                'snGradSchemes_default': 'corrected',
            },
        'decomposeParDict':
            {
                'numberOfSubdomains': '8',
                'method': 'scotch',
            },
        'fvSolution':
            {
                'E_solver': 'PCG',
                'E_preconditioner': 'DIC',
                'E_tolerance': '1e-06',
                'E_relTol': '0',
                'U_solver': 'PCG',
                'U_preconditioner': 'DIC',
                'U_tolerance': '1e-06',
                'U_relTol': '0',
                'SIMPLE_nNonOrthogonalCorrectors': '2',
            }
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
                'properties_rhoe': 'vapor_mass_fraction temperature pressure speed_of_sound viscosity thermal_conductivity',
                'properties_TP': 'vapor_mass_fraction density internal_energy speed_of_sound viscosity thermal_conductivity',
                'properties_TRho': '(vapor_volume_fraction)',
                'name': 'alphav',
                'type': 'AlphavTRho',
                'mixture_calculation_method': 'volume_average',
            },
        'g':
            {
                'value': '0 0 0',
            }
    }

zero = \
    {
        'infConditions':
            {
                'U_inf': '(0 0 0)',
                'p_inf': '300',
                'T_inf': '300',
                'alpha_inf': '1.0',
                'T_wall': '300',
                'p_nozzle': '3e+3',
                'T_nozzle': '700',
                'alpha_nozzle': '1.0'
            }
    }

files_data = {'system': system, 'constant': constant, '0.orig': zero}
