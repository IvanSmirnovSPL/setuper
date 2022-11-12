import argparse


# 'alpha'
# 'U'
# 'p'
# 'np'
# 'tolerance'
# 'relTol'
# 'momentumPredictor'
# 'nOuterCorrectors'
# 'nCorrectors'
# 'nNonOrthogonalCorrectors'
# 'U.*'
# 'Gllc'
# 'startFrom'
# 'startTime'
# 'stopAt'
# 'endTime'
# 'deltaT'
# 'writeControl'
# 'writeInterval'
# 'purgeWrite'
# 'writeFormat'
# 'writePrecision'
# 'writeCompression'
# 'timeFormat'
# 'runTimeModifiable'
# 'maxCo'

def unpackArg(arg, sep='_'):
    return " ".join(arg.split('_'))


def fillFromUserDict(userDict, files_data):
    for key in userDict.keys():
        #print(key, userDict[key], type(files_data['system']))
        if key == 'application':
            files_data['system']['controlDict']['application'] = str(userDict[key])
        elif key == 'startFrom':
            files_data['system']['controlDict']['startFrom'] = str(userDict[key])
        elif key == 'startTime':
            files_data['system']['controlDict']['startTime'] = str(userDict[key])
        elif key == 'stopAt':
            files_data['system']['controlDict']['stopAt'] = str(userDict[key])
        elif key == 'endTime':
            files_data['system']['controlDict']['endTime'] = str(userDict[key])
        elif key == 'deltaT':
            files_data['system']['controlDict']['deltaT'] = str(userDict[key])
        elif key == 'writeControl':
            files_data['system']['controlDict']['writeControl'] = str(userDict[key])
        elif key == 'writeInterval':
            files_data['system']['controlDict']['writeInterval'] = str(userDict[key])
        elif key == 'purgeWrite':
            files_data['system']['controlDict']['purgeWrite'] = str(userDict[key])
        elif key == 'writeFormat':
            files_data['system']['controlDict']['writeFormat'] = str(userDict[key])
        elif key == 'writePrecision':
            files_data['system']['controlDict']['writePrecision'] = str(userDict[key])
        elif key == 'writeCompression':
            files_data['system']['controlDict']['writeCompression'] = str(userDict[key])
        elif key == 'timeFormat':
            files_data['system']['controlDict']['timeFormat'] = str(userDict[key])
        elif key == 'timePrecision':
            files_data['system']['controlDict']['timePrecision'] = str(userDict[key])
        elif key == 'runTimeModifiable':
            files_data['system']['controlDict']['runTimeModifiable'] = str(userDict[key])
        elif key == 'adjustTimeStep':
            files_data['system']['controlDict']['adjustTimeStep'] = str(userDict[key])
        elif key == 'maxCo':
            files_data['system']['controlDict']['maxCo'] = str(userDict[key])
        elif key == 'maxDeltaT':
            files_data['system']['controlDict']['maxDeltaT'] = str(userDict[key])
            files_data['system']['fvSolution']['E_solver'] = str(userDict[key])
        elif key == 'U_inf':
            files_data['0.orig']['infConditions']['U_inf'] = str(userDict[key])
        elif key == 'p_inf':
            files_data['0.orig']['infConditions']['p_inf'] = str(userDict[key])
        elif key == 'T_inf':
            files_data['0.orig']['infConditions']['T_inf'] = str(userDict[key])
        elif key == 'alpha_inf':
            files_data['0.orig']['infConditions']['alpha_inf'] = str(userDict[key])
        elif key == 'T_wall':
            files_data['0.orig']['infConditions']['T_wall'] = str(userDict[key])
        elif key == 'p_nozzle':
            files_data['0.orig']['infConditions']['p_nozzle'] = str(userDict[key])
        elif key == 'T_nozzle':
            files_data['0.orig']['infConditions']['T_nozzle'] = str(userDict[key])
        elif key == 'alpha_nozzle':
            files_data['0.orig']['infConditions']['alpha_nozzle'] = str(userDict[key])
        elif key == 'value':
            files_data['constant']['g']['value'] = str(userDict[key])


def programmSettings(parser):
    parser.add_argument('-application', '--application', metavar='', type=str, default='FAKTFoam', help='')
    parser.add_argument('-startFrom', '--startFrom', metavar='', type=str, default='latestTime', help='')
    parser.add_argument('-startTime', '--startTime', metavar='', type=str, default='0', help='')
    parser.add_argument('-stopAt', '--stopAt', metavar='', type=str, default='endTime', help='')
    parser.add_argument('-endTime', '--endTime', metavar='', type=str, default='1e-2', help='')
    parser.add_argument('-deltaT', '--deltaT', metavar='', type=str, default='1e-07', help='')
    parser.add_argument('-writeControl', '--writeControl', metavar='', type=str, default='timeStep', help='')
    parser.add_argument('-writeInterval', '--writeInterval', metavar='', type=str, default='50', help='')
    parser.add_argument('-purgeWrite', '--purgeWrite', metavar='', type=str, default='0', help='')
    parser.add_argument('-writeFormat', '--writeFormat', metavar='', type=str, default='ascii', help='')
    parser.add_argument('-writePrecision', '--writePrecision', metavar='', type=str, default='6', help='')
    parser.add_argument('-writeCompression', '--writeCompression', metavar='', type=str, default='off', help='')
    parser.add_argument('-timeFormat', '--timeFormat', metavar='', type=str, default='general', help='')
    parser.add_argument('-timePrecision', '--timePrecision', metavar='', type=str, default='6', help='')
    parser.add_argument('-runTimeModifiable', '--runTimeModifiable', metavar='', type=str, default='true', help='')
    parser.add_argument('-adjustTimeStep', '--adjustTimeStep', metavar='', type=str, default='yes', help='')
    parser.add_argument('-maxCo', '--maxCo', metavar='', type=str, default='0.5', help='')
    parser.add_argument('-maxDeltaT', '--maxDeltaT', metavar='', type=str, default='1', help='')
    parser.add_argument('-value', '--value', metavar='', type=str, default='0 0 0', help='')
    parser.add_argument('-U_inf', '--U_inf', metavar='', type=str, default='0 0 0', help='')
    parser.add_argument('-p_inf', '--p_inf', metavar='', type=str, default='300', help='')
    parser.add_argument('-T_inf', '--T_inf', metavar='', type=str, default='300', help='')
    parser.add_argument('-alpha_inf', '--alpha_inf', metavar='', type=str, default='1.0', help='')
    parser.add_argument('-T_wall', '--T_wall', metavar='', type=str, default='300', help='')
    parser.add_argument('-p_nozzle', '--p_nozzle', metavar='', type=str, default='3e+3', help='')
    parser.add_argument('-T_nozzle', '--T_nozzle', metavar='', type=str, default='700', help='')
    parser.add_argument('-alpha_nozzle', '--alpha_nozzle', metavar='', type=str, default='1.0', help='')


def dictFromUserFlags(args):
    userDict = {}
    userDict['application'] = args.application
    userDict['startFrom'] = args.startFrom
    userDict['startTime'] = args.startTime
    userDict['stopAt'] = args.stopAt
    userDict['endTime'] = args.endTime
    userDict['deltaT'] = args.deltaT
    userDict['writeControl'] = args.writeControl
    userDict['writeInterval'] = args.writeInterval
    userDict['purgeWrite'] = args.purgeWrite
    userDict['writeFormat'] = args.writeFormat
    userDict['writePrecision'] = args.writePrecision
    userDict['writeCompression'] = args.writeCompression
    userDict['timeFormat'] = args.timeFormat
    userDict['timePrecision'] = args.timePrecision
    userDict['runTimeModifiable'] = args.runTimeModifiable
    userDict['adjustTimeStep'] = args.adjustTimeStep
    userDict['maxCo'] = args.maxCo
    userDict['maxDeltaT'] = args.maxDeltaT
    userDict['value'] = '(' + unpackArg(args.value) + ')'
    userDict['U_inf'] = '(' + unpackArg(args.U_inf) + ')'
    userDict['p_inf'] = args.p_inf
    userDict['T_inf'] = args.T_inf
    userDict['alpha_inf'] = args.alpha_inf
    userDict['T_wall'] = args.T_wall
    userDict['p_nozzle'] = args.p_nozzle
    userDict['T_nozzle'] = args.T_nozzle
    userDict['alpha_nozzle'] = args.alpha_nozzle
    return userDict


def userFlags():
    parser = argparse.ArgumentParser(description="A program for generating files for cavitation case")
    parser.add_argument('-n', '--name_case', metavar='', type=str, default='new_case', help="A path to case directory.")
    parser.add_argument('-vtk', '--vtk_path', metavar='', type=str, default='new_case_',
                        help="A path to vtk directory.")
    parser.add_argument('-grid', '--grid_path', metavar='', type=str, default='../polyMesh', help="A path to grid.")
    parser.add_argument('-table', '--table_path', metavar='', type=str, default='/opt/kpvm/ismirnov/bin/tables',
                        help="A path to table.")
    parser.add_argument('-zero', '--zero_path', metavar='', type=str, default='None', help="A path to zero.")
    parser.add_argument('-output', '--output_path', metavar='', type=str, default='output.txt', help="A path to log.")
    parser.add_argument('-clear', '--clear_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    parser.add_argument('-reconstruct', '--reconstruct_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    programmSettings(parser)
    return parser
