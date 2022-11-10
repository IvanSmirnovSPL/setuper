def fill_thermophysicalProperties(params):
    return     r'' + '\n' + \
     r'phases (vapour liquid);' + '\n' + \
     r'' + '\n' + \
     r'properties_rhoe (vapor_mass_fraction temperature pressure speed_of_sound viscosity thermal_conductivity);' + '\n' + \
     r'properties_TP (vapor_mass_fraction density internal_energy speed_of_sound viscosity thermal_conductivity);' + '\n' + \
     r'properties_TRho (vapor_volume_fraction);' + '\n' + \
     r'' + '\n' + \
     r'rhoe_settings' + '\n' + \
     r'{' + '\n' + \
     r'    vapor_mass_fraction' + '\n' + \
     r'    {' + '\n' + \
     r'        name    Q;' + '\n' + \
     r'        type    PropertyRhoeTable;' + '\n' + \
     r'    }' + '\n' + \
     r'    temperature' + '\n' + \
     r'    {' + '\n' + \
     r'        name    T;' + '\n' + \
     r'        type    PropertyRhoeTable;' + '\n' + \
     r'    }' + '\n' + \
     r'    pressure' + '\n' + \
     r'    {' + '\n' + \
     r'        name    p;' + '\n' + \
     r'        type    PropertyRhoeTable;' + '\n' + \
     r'    }' + '\n' + \
     r'    speed_of_sound' + '\n' + \
     r'    {' + '\n' + \
     r'        name    c;' + '\n' + \
     r'        type    PropertyRhoeTable;' + '\n' + \
     r'    }' + '\n' + \
     r'    viscosity' + '\n' + \
     r'    {' + '\n' + \
     r'        name    mu;' + '\n' + \
     r'        type    PropertyRhoeTable;' + '\n' + \
     r'    }' + '\n' + \
     r'    thermal_conductivity' + '\n' + \
     r'    {' + '\n' + \
     r'        name    kappa;' + '\n' + \
     r'        type    PropertyRhoeTable;' + '\n' + \
     r'    }' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'TP_settings' + '\n' + \
     r'{' + '\n' + \
     r'    vapor_mass_fraction' + '\n' + \
     r'    {' + '\n' + \
     r'        name    Q;' + '\n' + \
     r'        type    PropertyTPTable;' + '\n' + \
     r'        mixture_calculation_method table;' + '\n' + \
     r'    }' + '\n' + \
     r'    density' + '\n' + \
     r'    {' + '\n' + \
     r'        name    rho;' + '\n' + \
     r'        type    PropertyTPTable;' + '\n' + \
     r'        mixture_calculation_method volume_average;' + '\n' + \
     r'    }' + '\n' + \
     r'    internal_energy' + '\n' + \
     r'    {' + '\n' + \
     r'        name    e;' + '\n' + \
     r'        type    PropertyTPTable;' + '\n' + \
     r'        mixture_calculation_method mass_average;' + '\n' + \
     r'    }' + '\n' + \
     r'    speed_of_sound' + '\n' + \
     r'    {' + '\n' + \
     r'        name    c;' + '\n' + \
     r'        type    PropertyTPTable;' + '\n' + \
     r'        mixture_calculation_method table;' + '\n' + \
     r'    }' + '\n' + \
     r'    viscosity' + '\n' + \
     r'    {' + '\n' + \
     r'        name    mu;' + '\n' + \
     r'        type    PropertyTPTable;' + '\n' + \
     r'        mixture_calculation_method volume_average;' + '\n' + \
     r'    }' + '\n' + \
     r'    thermal_conductivity' + '\n' + \
     r'    {' + '\n' + \
     r'        name    kappa;' + '\n' + \
     r'        type    PropertyTPTable;' + '\n' + \
     r'        mixture_calculation_method volume_average;' + '\n' + \
     r'    }' + '\n' + \
     r'}' + '\n' + \
     r'' + '\n' + \
     r'TRho_settings' + '\n' + \
     r'{' + '\n' + \
     r'    vapor_volume_fraction' + '\n' + \
     r'    {' + '\n' + \
     r'        name    alphav;' + '\n' + \
     r'        type    AlphavTRho;' + '\n' + \
     r'    }' + '\n' + \
     r'}' + '\n '
