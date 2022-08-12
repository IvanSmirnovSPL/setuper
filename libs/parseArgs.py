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


def fillFromUserDict(userDict, files_data):
    for key in userDict.keys():
        if key == 'alpha':
            files_data['0.orig']['alpha.water']['internal_value'] = str(userDict[key])
        elif key == 'U':
            files_data['0.orig']['U']['internal_value'] = str(userDict[key])
        elif key == 'p':
            files_data['0.orig']['p_rgh']['internal_value'] = str(userDict[key])
        elif key == 'np':
            files_data['system']['decomposeParDict']['numberOfSubdomains'] = str(userDict[key])
        elif key == 'tolerance':
            files_data['system']['fvSolution']['tolerance'] = str(userDict[key])
        elif key == 'relTol':
            files_data['system']['fvSolution']['relTol'] = str(userDict[key])
        elif key == 'momentumPredictor':
            files_data['system']['fvSolution']['momentumPredictor'] = str(userDict[key])
        elif key == 'nOuterCorrectors':
            files_data['system']['fvSolution']['nOuterCorrectors'] = str(userDict[key])
        elif key == 'nCorrectors':
            files_data['system']['fvSolution']['nCorrectors'] = str(userDict[key])
        elif key == 'nNonOrthogonalCorrectors':
            files_data['system']['fvSolution']['nNonOrthogonalCorrectors'] = str(userDict[key])
        elif key == 'U.*':
            files_data['system']['fvSolution']['U.*'] = str(userDict[key])
        elif key == 'Gllc':
            files_data['system']['fvSchemes']['Gllc'] = str(userDict[key])
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
        elif key == 'runTimeModifiable':
            files_data['system']['controlDict']['runTimeModifiable'] = str(userDict[key])
        elif key == 'maxCo':
            files_data['system']['controlDict']['maxCo'] = str(userDict[key])
        elif key == 'adjustTimeStep':
            files_data['system']['controlDict']['adjustTimeStep'] = str(userDict[key])


def programmSettings(parser):
    parser.add_argument('-a', '--alpha', metavar='', type=str, default='1', help="alpha.water")
    parser.add_argument('-U', '--U', metavar='', type=str, default='(0 0 20)', help="U")
    parser.add_argument('-p', '--p', metavar='', type=str, default='100000', help="p")
    parser.add_argument('-np', '--np', metavar='', type=str, default='1', help="Number of processes.")
    parser.add_argument('-tol', '--tolerance', metavar='', type=str, default='1e-6', help="tolerance")
    parser.add_argument('-relTol', '--relTol', metavar='', type=str, default='0.1', help="relTol")
    parser.add_argument('-mP', '--momentumPredictor', metavar='', type=str, default='no', help="momentumPredictor")
    parser.add_argument('-nOC', '--nOuterCorrectors', metavar='', type=str, default='1', help="nOuterCorrectors")
    parser.add_argument('-nC', '--nCorrectors', metavar='', type=str, default='3', help="nCorrectors")
    parser.add_argument('-nNOC', '--nNonOrthogonalCorrectors', metavar='', type=str, default='0',
                        help="nNonOrthogonalCorrectors")
    parser.add_argument('-rF', '--rF', metavar='', type=str, default='1', help="Relaxation factors, equations, 'U.*'")
    parser.add_argument('-Gllc', '--Gllc', metavar='', type=str, default='0.5', help="Gauss linear limited corrector.")
    parser.add_argument('-sF', '--startFrom', metavar='', type=str, default='latestTime', help="startFrom")
    parser.add_argument('-sT', '--startTime', metavar='', type=str, default='0', help="startTime")
    parser.add_argument('-sA', '--stopAt', metavar='', type=str, default='endTime', help="stopAt")
    parser.add_argument('-eT', '--endTime', metavar='', type=str, default='0.05', help="endTime")
    parser.add_argument('-dT', '--deltaT', metavar='', type=str, default='1e-8', help="deltaT")
    parser.add_argument('-wCon', '--writeControl', metavar='', type=str, default='adjustable', help="writeControl")
    parser.add_argument('-wI', '--writeInterval', metavar='', type=str, default='0.001', help="writeInterval")
    parser.add_argument('-wCom', '--writeCompression', metavar='', type=str, default='off',
                        help="writeCompression")
    parser.add_argument('-pW', '--purgeWrite', metavar='', type=str, default='0', help="purgeWrite")
    parser.add_argument('-wF', '--writeFormat', metavar='', type=str, default='ascii', help="writeFormat")
    parser.add_argument('-wP', '--writePrecision', metavar='', type=str, default='6', help="writePrecision")
    parser.add_argument('-tF', '--timeFormat', metavar='', type=str, default='general', help="timeFormat")
    parser.add_argument('-rTM', '--runTimeModifiable', metavar='', type=str, default='yes', help="runTimeModifiable")
    parser.add_argument('-aTS', '--adjustTimeStep', metavar='', type=str, default='on', help="adjustTimeStep")
    parser.add_argument('-mC', '--maxCo', metavar='', type=str, default='5', help="maxCo")


def dictFromUserFlags(args):
    userDict = {}
    userDict['alpha'] = args.alpha
    userDict['U'] = args.U
    userDict['p'] = args.p
    userDict['np'] = args.np
    userDict['tolerance'] = args.tolerance
    userDict['relTol'] = args.relTol
    userDict['momentumPredictor'] = args.momentumPredictor
    userDict['nOuterCorrectors'] = args.nOuterCorrectors
    userDict['nCorrectors'] = args.nCorrectors
    userDict['nNonOrthogonalCorrectors'] = args.nNonOrthogonalCorrectors
    userDict['U.*'] = args.rF
    userDict['Gllc'] = args.Gllc
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
    userDict['runTimeModifiable'] = args.runTimeModifiable
    userDict['maxCo'] = args.maxCo

    return userDict


def userFlags():
    parser = argparse.ArgumentParser(description="A program for generating files for cavitation case")
    parser.add_argument('-n', '--name_case', metavar='', type=str, default='new_case', help="A path to case directory.")
    parser.add_argument('-grid', '--grid_path', metavar='', type=str, default='../polyMesh', help="A path to grid.")
    parser.add_argument('-output', '--output_path', metavar='', type=str, default='output.txt', help="A path to log.")
    parser.add_argument('-clear', '--clear_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    parser.add_argument('-reconstract', '--reconstract_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    programmSettings(parser)
    return parser
