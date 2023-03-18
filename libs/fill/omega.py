def fill_omega(params, fn=None, fp=None):
    res = '' + '\n' + \
          'dimensions      [0 0 -1 0 0 0 0];' + '\n' + \
          '' + '\n' + \
          'internalField   uniform {};'.format(params['omega']) + '\n' + \
          '' + '\n' + \
          'boundaryField' + '\n' + \
          '{' + '\n' + \
          r'"(inlet).*" ' + '\n' + \
          '    {' + '\n' + \
          '        type            turbulentMixingLengthFrequencyInlet;' + '\n' + \
          '        mixingLength    0.0005;' + '\n' + \
          '        k               k;' + '\n' + \
          '        value           uniform {};'.format(params['omega']) + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          r'"(outlet).*" ' + '\n' + \
          '    {' + '\n' + \
          '        type            zeroGradient;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          r' "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*" ' + '\n' + \
          '    {' + '\n' + \
          '        type            omegaWallFunction;' + '\n' + \
          '        value           uniform {};'.format(params['omega']) + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '"(symmetry).*" ' + '\n' + \
          '{ ' + '\n' + \
          '  type      symmetry;' + '\n' + \
          '}' + '\n' + \
          '"(wedge).*" ' + '\n' + \
          '{ ' + '\n' + \
          '  type      wedge;' + '\n' + \
          '}' + '\n' + \
          '}' + '\n' + \
          '' + '\n' + \
          '' + '\n' + \
          '// ************************************************************************* //' + '\n'

    print(res, file=fp)
