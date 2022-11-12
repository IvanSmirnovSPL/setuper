def writeAlpha():
    return r'FoamFile' + '\n' + \
           r'{' + '\n' + \
           r'    version     2.0;' + '\n' + \
           r'    format      ascii;' + '\n' + \
           r'    class       volScalarField;' + '\n' + \
           r'    object      alpha.vapour;' + '\n' + \
           r'}' + '\n' + \
           r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
           r'' + '\n' + \
           r'#include "infConditions"' + '\n' + \
           r'' + '\n' + \
           r'dimensions [0 0 0 0 0 0 0];' + '\n' + \
           r'' + '\n' + \
           r'internalField uniform $alpha_inf;' + '\n' + \
           r'' + '\n' + \
           r'boundaryField' + '\n' + \
           r'{' + '\n' + \
           r'    inlet_l' + '\n' + \
           r'    {' + '\n' + \
           r'	type	fixedValue;' + '\n' + \
           r'	value	uniform $alpha_inf;' + '\n' + \
           r'    }' + '\n' + \
           r'    outlet' + '\n' + \
           r'    {' + '\n' + \
           r'	type    zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    outlet_2' + '\n' + \
           r'    {' + '\n' + \
           r'	type	symmetry;' + '\n' + \
           r'    }' + '\n' + \
           r'    wall' + '\n' + \
           r'    {' + '\n' + \
           r'	type	zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    inlet_g' + '\n' + \
           r'    {' + '\n' + \
           r'	type	fixedValue;' + '\n' + \
           r'	value	uniform $alpha_nozzle;	' + '\n' + \
           r'    }' + '\n' + \
           r'' + '\n' + \
           r'    frontAndBack' + '\n' + \
           r'    {' + '\n' + \
           r'        type            empty;' + '\n' + \
           r'    }' + '\n' + \
           r'}' + '\n '


def writeP():
    return r'FoamFile' + '\n' + \
           r'{' + '\n' + \
           r'    version     2.0;' + '\n' + \
           r'    format      ascii;' + '\n' + \
           r'    arch        "LSB;label=32;scalar=64";' + '\n' + \
           r'    class       volScalarField;' + '\n' + \
           r'    location    "0";' + '\n' + \
           r'    object      p;' + '\n' + \
           r'}' + '\n' + \
           r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
           r'' + '\n' + \
           r'#include "infConditions"' + '\n' + \
           r'' + '\n' + \
           r'dimensions      [1 -1 -2 0 0 0 0];' + '\n' + \
           r'' + '\n' + \
           r'internalField   uniform $p_inf;' + '\n' + \
           r'' + '\n' + \
           r'boundaryField' + '\n' + \
           r'{' + '\n' + \
           r'    wall' + '\n' + \
           r'    {' + '\n' + \
           r'        type            zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    inlet_l' + '\n' + \
           r'    {' + '\n' + \
           r'        type            fixedValue;' + '\n' + \
           r'        value           $internalField;' + '\n' + \
           r'    }' + '\n' + \
           r'    inlet_g' + '\n' + \
           r'    {' + '\n' + \
           r'        type            fixedValue;' + '\n' + \
           r'        value           uniform $p_nozzle; // 1.3e+05; //  ' + '\n' + \
           r'    }' + '\n' + \
           r'    outlet' + '\n' + \
           r'    {' + '\n' + \
           r'        type            zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    frontAndBack' + '\n' + \
           r'    {' + '\n' + \
           r'        type            empty;' + '\n' + \
           r'    }' + '\n' + \
           r'}' + '\n' + \
           r'' + '\n' + \
           r'' + '\n' + \
           r'// ************************************************************************* //' + '\n '


def writeT():
    return r'FoamFile' + '\n' + \
           r'{' + '\n' + \
           r'    version     2.0;' + '\n' + \
           r'    format      ascii;' + '\n' + \
           r'    arch        "LSB;label=32;scalar=64";' + '\n' + \
           r'    class       volScalarField;' + '\n' + \
           r'    location    "0";' + '\n' + \
           r'    object      T;' + '\n' + \
           r'}' + '\n' + \
           r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
           r'' + '\n' + \
           r'#include "infConditions"' + '\n' + \
           r'' + '\n' + \
           r'dimensions      [0 0 0 1 0 0 0];' + '\n' + \
           r'' + '\n' + \
           r'internalField   uniform $T_inf;' + '\n' + \
           r'' + '\n' + \
           r'boundaryField' + '\n' + \
           r'{' + '\n' + \
           r'    wall' + '\n' + \
           r'    {' + '\n' + \
           r'        type            zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    inlet_l' + '\n' + \
           r'    {' + '\n' + \
           r'        type            fixedValue;' + '\n' + \
           r'        value           uniform $T_inf;' + '\n' + \
           r'    }' + '\n' + \
           r'    inlet_g' + '\n' + \
           r'    {' + '\n' + \
           r'        type            fixedValue;' + '\n' + \
           r'        value           uniform $T_nozzle;' + '\n' + \
           r'    }' + '\n' + \
           r'    outlet' + '\n' + \
           r'    {' + '\n' + \
           r'        type            zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    frontAndBack' + '\n' + \
           r'    {' + '\n' + \
           r'        type            empty;' + '\n' + \
           r'    }' + '\n' + \
           r'}' + '\n' + \
           r'' + '\n' + \
           r'' + '\n' + \
           r'// ************************************************************************* //' + '\n '


def writeU():
    return r'FoamFile' + '\n' + \
           r'{' + '\n' + \
           r'    version     2.0;' + '\n' + \
           r'    format      ascii;' + '\n' + \
           r'    class       volVectorField;' + '\n' + \
           r'    object      U;' + '\n' + \
           r'}' + '\n' + \
           r'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //' + '\n' + \
           r'' + '\n' + \
           r'#include "infConditions"' + '\n' + \
           r'' + '\n' + \
           r'dimensions      [0 1 -1 0 0 0 0];' + '\n' + \
           r'' + '\n' + \
           r'internalField   uniform $U_inf;' + '\n' + \
           r'' + '\n' + \
           r'boundaryField' + '\n' + \
           r'{' + '\n' + \
           r'    inlet_l' + '\n' + \
           r'    {' + '\n' + \
           r'      type	inletOutlet; //fixedValue;' + '\n' + \
           r'      inletValue $internalField;' + '\n' + \
           r'      value   $internalField;' + '\n' + \
           r'    }' + '\n' + \
           r'    outlet' + '\n' + \
           r'    {' + '\n' + \
           r'	type	zeroGradient;' + '\n' + \
           r'    }' + '\n' + \
           r'    outlet_2' + '\n' + \
           r'    {' + '\n' + \
           r'	type	symmetry;' + '\n' + \
           r'    }' + '\n' + \
           r'    wall' + '\n' + \
           r'    {' + '\n' + \
           r'	type	noSlip;' + '\n' + \
           r'    }' + '\n' + \
           r'    inlet_g' + '\n' + \
           r'    {' + '\n' + \
           r'      type    zeroGradient; //surfaceNormalFixedValue;' + '\n' + \
           r'	' + '\n' + \
           r'      //	refValue      uniform -10;	' + '\n' + \
           r'    }' + '\n' + \
           r'' + '\n' + \
           r'    frontAndBack' + '\n' + \
           r'    {' + '\n' + \
           r'        type            empty;' + '\n' + \
           r'    }' + '\n' + \
           r'}' + '\n' + \
           r'' + '\n' + \
           r'' + '\n' + \
           r'// ************************************************************************* //' + '\n '


def writeInfConditions(params):
    return r'' + '\n' + \
       r'U_inf            {};'.format(params['U_inf']) + '\n' + \
           r'p_inf            {};'.format(params['p_inf']) + '\n' + \
           r'T_inf            {};'.format(params['T_inf']) + '\n' + \
           r'alpha_inf        {};'.format(params['alpha_inf']) + '\n' + \
           r'T_wall		 {};'.format(params['T_wall']) + '\n' + \
           r'' + '\n' + \
           r'p_nozzle	 {};'.format(params['p_nozzle']) + '\n' + \
           r'T_nozzle	 {};'.format(params['T_nozzle']) + '\n' + \
           r'alpha_nozzle     {};'.format(params['alpha_nozzle']) + '\n' + \
           r'' + '\n' + \
           r'' + '\n' + \
           r'#inputMode   merge' + '\n' + \
           r'' + '\n' + \
           r'// ************************************************************************* //' + '\n '
