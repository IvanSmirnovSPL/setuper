def fill_thermophysicalProperties(params):
    return      '' + '\n' + \
     r'properties_rhoe ({});'.format(params['properties_rhoe']) + '\n' + \
     r'properties_TP ({});'.format(params['properties_TP']) + '\n' + \
     r'properties_TRho ({});'.format(params['properties_TRho']) + '\n' + \
     '' + '\n' + \
     'rhoe_settings' + '\n' + \
     '{' + '\n' + \
     '    vapor_mass_fraction' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '    temperature' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '    pressure' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '    speed_of_sound' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '    viscosity' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '    thermal_conductivity' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'TP_settings' + '\n' + \
     '{' + '\n' + \
     '    vapor_mass_fraction' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    }' + '\n' + \
     '    density' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    }' + '\n' + \
     '    internal_energy' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    }' + '\n' + \
     '    speed_of_sound' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    }' + '\n' + \
     '    viscosity' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    }' + '\n' + \
     '    thermal_conductivity' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    }' + '\n' + \
     '}' + '\n' + \
     '' + '\n' + \
     'TRho_settings' + '\n' + \
     '{' + '\n' + \
     '    vapor_volume_fraction' + '\n' + \
     '    {' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    }' + '\n' + \
     '}' + '\n '
