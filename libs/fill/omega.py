def fill_omega(params, fn=None, fp=None):
    res = '' + '\n' + \
          'dimensions      [0 0 -1 0 0 0 0];' + '\n' + \
          '' + '\n' + \
          'internalField   uniform {};'.format(params['omega']) + '\n' + \
          '' + '\n' + \
          'boundaryField' + '\n' + \
          '{' + '\n' + \
          '    inlet' + '\n' + \
          '    {' + '\n' + \
          '        type            turbulentMixingLengthFrequencyInlet;' + '\n' + \
          '        mixingLength    0.0005;' + '\n' + \
          '        k               k;' + '\n' + \
          '        value           uniform {};'.format(params['omega']) + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    outlet' + '\n' + \
          '    {' + '\n' + \
          '        type            zeroGradient;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    walls' + '\n' + \
          '    {' + '\n' + \
          '        type            omegaWallFunction;' + '\n' + \
          '        value           uniform {};'.format(params['omega']) + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    frontBack' + '\n' + \
          '    {' + '\n' + \
          '        type            empty;' + '\n' + \
          '    }' + '\n' + \
          '}' + '\n' + \
          '' + '\n' + \
          '' + '\n' + \
          '// ************************************************************************* //' + '\n'

    print(res, file=fp)
