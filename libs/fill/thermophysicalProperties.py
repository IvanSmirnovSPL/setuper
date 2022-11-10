def fill_thermophysicalProperties(params):
    return      r'FoamFile' + '\n' + \
     r'{' + '\n' + \
     r'    version     2.0;' + '\n' + \
     r'    format      ascii;' + '\n' + \
     r'    class       dictionary;' + '\n' + \
     r'    location    "constant";' + '\n' + \
     r'    object      thermophysicalProperties;' + '\n' + \
     r'}' + '\n' + \
     r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
     '' + '\n' + \
     r'phases ({});'.format(params['phases']) + '\n' + \
     '' + '\n' + \
     r'properties_rhoe ({});'.format(params['properties_rhoe']) + '\n' + \
     r'properties_TP ({});'.format(params['properties_TP']) + '\n' + \
     r'properties_TRho ({});'.format(params['properties_TRho']) + '\n' + \
     '' + '\n' + \
     'rhoe_setting' + '\n' + \
     '' + '\n' + \
     '    vapor_mass_fractio' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '    temperatur' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '    pressur' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '    speed_of_soun' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '    viscosit' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '    thermal_conductivit' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'TP_setting' + '\n' + \
     '' + '\n' + \
     '    vapor_mass_fractio' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    ' + '\n' + \
     '    densit' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    ' + '\n' + \
     '    internal_energ' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    ' + '\n' + \
     '    speed_of_soun' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    ' + '\n' + \
     '    viscosit' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    ' + '\n' + \
     '    thermal_conductivit' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     r'mixture_calculation_method {};'.format(params['mixture_calculation_method']) + '\n' + \
     '    ' + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     'TRho_setting' + '\n' + \
     '' + '\n' + \
     '    vapor_volume_fractio' + '\n' + \
     '    ' + '\n' + \
     r'name {};'.format(params['name']) + '\n' + \
     r'type {};'.format(params['type']) + '\n' + \
     '    ' + '\n' + \
     '' + '\n '
