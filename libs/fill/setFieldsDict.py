def fill_SetFieldsDict(params):
    return  '// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //  \n' + \
           '  \n' + \
           '#include "params"  \n' + \
           'half_a  #calc "$a/2.0";  \n' + \
           'half_L  #calc "$L/2.0";  \n' + \
           '  \n' + \
           'defaultFieldValues  \n' + \
           '(  \n' + \
           '    volVectorFieldValue U (0 0 0)  \n' + \
           '    volScalarFieldValue T 10  \n' + \
           '    volScalarFieldValue p 1  \n' + \
           ');  \n' + \
           '  \n' + \
           'regions  \n' + \
           '(  \n' + \
           '    boxToCell  \n' + \
           '    {  \n' + \
           '        box (-$half_L -$half_a -$half_a) ($shift $half_a $half_a);  \n' + \
           '        fieldValues  \n' + \
           '        (  \n' + \
           '            volScalarFieldValue T $T_left  \n' + \
           '            volScalarFieldValue p $p_left  \n' + \
           '            volScalarFieldValue alpha.vapour $alpha_left  \n' + \
           '            volVectorFieldValue U $U_left  \n' + \
           '        );  \n' + \
           '    }  \n' + \
           '    boxToCell  \n' + \
           '    {  \n' + \
           '        box ($shift -$half_a -$half_a) ($half_L $half_a $half_a);  \n' + \
           '        fieldValues  \n' + \
           '        (  \n' + \
           '            volScalarFieldValue T $T_right  \n' + \
           '            volScalarFieldValue p $p_right  \n' + \
           '            volScalarFieldValue alpha.vapour $alpha_right  \n' + \
           '            volVectorFieldValue U $U_right  \n' + \
           '        );  \n' + \
           '    }  \n' + \
           ');  \n' + \
           '  \n' + \
           '  \n' + \
           '// ************************************************************************* //  \n'
