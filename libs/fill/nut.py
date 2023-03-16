def fill_nut(params, fn=None, fp=None):
    res = '' + '\n' + \
          'dimensions[0 2 - 1 0 0 0 0];' + '\n' + \
          '' + '\n' + \
          'internalField   uniform 0;' + '\n' + \
          '' + '\n' + \
          'boundaryField' + '\n' + \
          '{' + '\n' + \
          '    inlet' + '\n' + \
          '    {' + '\n' + \
          '        type            calculated;' + '\n' + \
          '        value           uniform 0;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    outlet' + '\n' + \
          '    {' + '\n' + \
          '        type            calculated;' + '\n' + \
          '        value           uniform 0;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          '    walls' + '\n' + \
          '    {' + '\n' + \
          '        type            nutkWallFunction;' + '\n' + \
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
