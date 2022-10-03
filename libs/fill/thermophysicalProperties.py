def fill_thermophysicalProperties(param):
    return '  \n' + \
           ' phases ( {} ); \n'.format(param['phases']) + \
           '  \n' + \
           'properties_rhoe (vapor_mass_fraction temperature pressure speed_of_sound viscosity thermal_conductivity); \n' + \
           'properties_TP (vapor_mass_fraction density internal_energy speed_of_sound viscosity thermal_conductivity); \n' + \
           ' \n' + \
            'rhoe_settings \n' + \
            '{ \n' + \
            '    vapor_mass_fraction \n' + \
            '    { \n' + \
            '        name    Q; \n' + \
            '        type    PropertyRhoeTable; \n' + \
            '    } \n' + \
            '    temperature \n' + \
            '    { \n' + \
            '        name    T; \n' + \
            '        type    PropertyRhoeTable; \n' + \
            '    } \n' + \
            '    pressure \n' + \
            '    { \n' + \
            '        name    p; \n' + \
            '        type    PropertyRhoeTable; \n' + \
            '    } \n' + \
            '    speed_of_sound \n' + \
            '    { \n' + \
            '        name    c; \n' + \
            '        type    PropertyRhoeTable; \n' + \
            '    } \n' + \
            '    viscosity \n' + \
            '    { \n' + \
            '        name    mu; \n' + \
            '        type    PropertyRhoeTable; \n' + \
            '    } \n' + \
            '    thermal_conductivity \n' + \
            '    { \n' + \
            '        name    kappa; \n' + \
            '        type    PropertyRhoeTable; \n' + \
            '    } \n' + \
            '} \n' + \
            ' \n' + \
            'TP_settings \n' + \
            '{ \n' + \
            '    vapor_mass_fraction \n' + \
            '    { \n' + \
            '        name    Q; \n' + \
            '        type    PropertyTPTable; \n' + \
            '        mixture_calculation_method table; \n' + \
            '    } \n' + \
            '    density \n' + \
            '    { \n' + \
            '        name    rho; \n' + \
            '        type    PropertyTPTable; \n' + \
            '        mixture_calculation_method volume_average; \n' + \
            '    } \n' + \
            '    internal_energy \n' + \
            '    { \n' + \
            '        name    e; \n' + \
            '        type    PropertyTPTable; \n' + \
            '        mixture_calculation_method mass_average; \n' + \
            '    } \n' + \
            '    speed_of_sound \n' + \
            '    { \n' + \
            '        name    c; \n' + \
            '        type    PropertyTPTable; \n' + \
            '        mixture_calculation_method table; \n' + \
            '    } \n' + \
            '    viscosity \n' + \
            '    { \n' + \
            '        name    mu; \n' + \
            '        type    PropertyTPTable; \n' + \
            '        mixture_calculation_method volume_average; \n' + \
            '    } \n' + \
            '    thermal_conductivity \n' + \
            '    { \n' + \
            '        name    kappa; \n' + \
            '        type    PropertyTPTable; \n' + \
            '        mixture_calculation_method volume_average; \n' + \
            '    } \n' + \
            '} \n'