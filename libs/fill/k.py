def fill_k(params, fn=None, fp=None):
    res = '' + '\n' + \
          'dimensions      [0 2 -2 0 0 0 0];' + '\n' + \
          '' + '\n' + \
          'internalField   uniform {}; // calc from U ( k = 3/2*(I*U_inf)**2), Intensity'.format(params['k']) + '\n' + \
          '' + '\n' + \
          'boundaryField' + '\n' + \
          '{' + '\n' + \
          '    inlet' + '\n' + \
          '    {' + '\n' + \
          '        type            turbulentIntensityKineticEnergyInlet;' + '\n' + \
          '        intensity       {}; // egorych Intensity'.format(params['intensity']) + '\n' + \
          '        value           uniform 0.05;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    outlet' + '\n' + \
          '    {' + '\n' + \
          '        type            zeroGradient;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    walls' + '\n' + \
          '    {' + '\n' + \
          '        type            fixedValue; //kqRWallFunction;' + '\n' + \
          '        value           uniform 0;' + '\n' + \
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
