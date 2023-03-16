
def fill_turbulenceProperties(params):
    turbulence_prop = '' + '\n' + \
                      'RAS' + '\n' + \
                      '{' + '\n' + \
                      '    RASModel        kOmegaSST;' + '\n' + \
                      '' + '\n' + \
                      '    turbulence      on;' + '\n' + \
                      '' + '\n' + \
                      '    printCoeffs     on;' + '\n' + \
                      '}' + '\n'
    if not params["turbulence"]:
        return 'simulationType      laminar;' + '\n'
    else:
        return 'simulationType      RAS;' + '\n' + turbulence_prop
