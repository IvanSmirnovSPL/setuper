def fill_nut(params, fn=None, fp=None):
    res = '' + '\n' + \
          'dimensions     [0 2 -1 0 0 0 0];' + '\n' + \
          '' + '\n' + \
          'internalField   uniform 0;' + '\n' + \
          '' + '\n' + \
          'boundaryField' + '\n' + \
          '{' + '\n' + \
          r'"(inlet).*" ' + '\n' + \
          '    {' + '\n' + \
          '        type            calculated;' + '\n' + \
          '        value           uniform 0;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          r'"(outlet).*" ' + '\n' + \
          '    {' + '\n' + \
          '        type            calculated;' + '\n' + \
          '        value           uniform 0;' + '\n' + \
          '    }' + '\n' + \
          '' + '\n' + \
          r' "(wall|WALL|Wall|originalPatch|Created|walls|WALLS|Walls).*" ' + '\n' + \
          '    {' + '\n' + \
          '        type            nutkWallFunction;' + '\n' + \
          '        value           uniform 0;' + '\n' + \
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
