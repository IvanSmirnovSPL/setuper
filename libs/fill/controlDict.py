def fill_controlDict(params):
    return      r'FoamFile' + '\n' + \
     r'{' + '\n' + \
     r'    version     2.0;' + '\n' + \
     r'    format      ascii;' + '\n' + \
     r'    class       dictionary;' + '\n' + \
     r'    location    "system";' + '\n' + \
     r'    object      controlDict;' + '\n' + \
     r'}' + '\n' + \
     r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
     '' + '\n' + \
     r'application {};'.format(params['application']) + '\n' + \
     '' + '\n' + \
     r'startFrom {};'.format(params['startFrom']) + '\n' + \
     '' + '\n' + \
     r'startTime {};'.format(params['startTime']) + '\n' + \
     '' + '\n' + \
     r'stopAt {};'.format(params['stopAt']) + '\n' + \
     '' + '\n' + \
     r'endTime {};'.format(params['endTime']) + '\n' + \
     '' + '\n' + \
     r'deltaT {};'.format(params['deltaT']) + '\n' + \
     '' + '\n' + \
     r'writeControl {};'.format(params['writeControl']) + '\n' + \
     '' + '\n' + \
     r'writeInterval {};'.format(params['writeInterval']) + '\n' + \
     '' + '\n' + \
     r'purgeWrite {};'.format(params['purgeWrite']) + '\n' + \
     '' + '\n' + \
     r'writeFormat {};'.format(params['writeFormat']) + '\n' + \
     '' + '\n' + \
     r'writePrecision {};'.format(params['writePrecision']) + '\n' + \
     '' + '\n' + \
     r'writeCompression {};'.format(params['writeCompression']) + '\n' + \
     '' + '\n' + \
     r'timeFormat {};'.format(params['timeFormat']) + '\n' + \
     '' + '\n' + \
     r'timePrecision {};'.format(params['timePrecision']) + '\n' + \
     '' + '\n' + \
     r'runTimeModifiable {};'.format(params['runTimeModifiable']) + '\n' + \
     '' + '\n' + \
     r'adjustTimeStep {};'.format(params['adjustTimeStep']) + '\n' + \
     '' + '\n' + \
     r'maxCo {};'.format(params['maxCo']) + '\n' + \
     '' + '\n' + \
     r'maxDeltaT {};'.format(params['maxDeltaT']) + '\n' + \
     '' + '\n' + \
     '' + '\n' + \
     '// ************************************************************************* /' + '\n '
