import argparse
import numpy as np

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
        if key == 'alpha':
            files_data['0.orig']['alpha.water']['internal_value'] = str(userDict[key])
        elif key == 'U':
            files_data['0.orig']['U']['internal_value'] = '(' + str(unpackArg(userDict['U_LBC_vo'])) + ')'
        elif key == 'p':
            files_data['0.orig']['p_rgh']['internal_value'] = userDict['p_LBC_vo']
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
        elif key == 'g':
            files_data['constant']['g']['g'] = str(userDict[key])
        elif key == 'pSat':
            files_data['constant']['transportProperties']['pSat'] = str(userDict[key])
        elif key == 'U_LBC':
            files_data['0.orig']['U']['linearBC'] = userDict[key]
        elif key == 'U_LBC_faces':
            files_data['0.orig']['U']['faces'] = userDict[key].split('_')
        elif key == 'U_LBC_to':
            files_data['0.orig']['U']['to'] = userDict[key]
        elif key == 'U_LBC_tf':
            files_data['0.orig']['U']['tf'] = userDict[key]
        elif key == 'U_LBC_vo':
            files_data['0.orig']['U']['vo'] = userDict[key]
        elif key == 'U_LBC_vf':
            files_data['0.orig']['U']['vf'] = userDict[key]
        elif key == 'p_LBC':
            files_data['0.orig']['p_rgh']['linearBC'] = userDict[key]
        elif key == 'p_LBC_faces':
            files_data['0.orig']['p_rgh']['faces'] = userDict[key].split('_')
        elif key == 'p_LBC_to':
            files_data['0.orig']['p_rgh']['to'] = userDict[key]
        elif key == 'p_LBC_tf':
            files_data['0.orig']['p_rgh']['tf'] = userDict[key]
        elif key == 'p_LBC_vo':
            files_data['0.orig']['p_rgh']['vo'] = userDict[key]
        elif key == 'p_LBC_vf':
            files_data['0.orig']['p_rgh']['vf'] = userDict[key]
        elif key == 'turbulence':
            files_data['constant']['turbulenceProperties']['turbulence'] = userDict[key]
        elif key == 'intensity':
            files_data['0.orig']['k']['intensity'] = userDict[key]
        elif key == 'omega':
            files_data['0.orig']['omega']['omega'] = userDict[key]
        elif key == 'k':
            u = np.linalg.norm(list(map(lambda t: float(t), files_data['0.orig']['U']['internal_value'][1:-1].split(' '))))
            files_data['0.orig']['k']['k'] = 1.5 * (float(files_data['0.orig']['k']['intensity']) * u) ** 2





def programmSettings(parser):
    parser.add_argument('-a', '--alpha', metavar='', type=str, default='1', help="alpha.water")
    parser.add_argument('-U', '--U', metavar='', type=str, default='0_0_-20', help="U")
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
    parser.add_argument('-g', '--g', metavar='', type=str, default='0_-9.81_0', help="g")
    parser.add_argument('-pSat', '--pSat', metavar='', type=str, default='2300', help="Saturation pressure")

    parser.add_argument('-U_LBC', '--U_LBC', metavar='', type=bool, default=True, help="linearBC")
    parser.add_argument('-U_LBC_faces', '--U_LBC_faces', metavar='', type=str, default='inlet', help="linearBC_faces")
    parser.add_argument('-U_LBC_to', '--U_LBC_to', metavar='', type=str, default=0, help="linearBC_to")
    parser.add_argument('-U_LBC_tf', '--U_LBC_tf', metavar='', type=str, default=0, help="linearBC_tf")
    parser.add_argument('-U_LBC_vo', '--U_LBC_vo', metavar='', type=str, default='0_0_0', help="linearBC_vo")
    parser.add_argument('-U_LBC_vf', '--U_LBC_vf', metavar='', type=str, default='0_0_0', help="linearBC_vf")

    parser.add_argument('-p_LBC', '--p_LBC', metavar='', type=bool, default=True, help="linearBC")
    parser.add_argument('-p_LBC_faces', '--p_LBC_faces', metavar='', type=str, default='inlet', help="linearBC_faces")
    parser.add_argument('-p_LBC_to', '--p_LBC_to', metavar='', type=str, default=0, help="linearBC_to")
    parser.add_argument('-p_LBC_tf', '--p_LBC_tf', metavar='', type=str, default=0, help="linearBC_tf")
    parser.add_argument('-p_LBC_vo', '--p_LBC_vo', metavar='', type=str, default=0, help="linearBC_vo")
    parser.add_argument('-p_LBC_vf', '--p_LBC_vf', metavar='', type=str, default=0, help="linearBC_vf")

    parser.add_argument('-turbulence', '--turbulence', metavar='', type=int, default=0, help="turbulence")

    parser.add_argument('-intensity', '--intensity', metavar='', type=str, default='0.05', help="intensity")
    parser.add_argument('-omega', '--omega', metavar='', type=str, default='80000', help="omega")

def dictFromUserFlags(args):
    userDict = {}
    userDict['pSat'] = args.pSat
    userDict['alpha'] = args.alpha
    userDict['U'] = '(' + unpackArg(args.U) + ')'
    userDict['g'] = unpackArg(args.g)
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

    userDict['U_LBC'] = args.U_LBC
    userDict['U_LBC_faces'] = args.U_LBC_faces
    userDict['U_LBC_to'] = args.U_LBC_to
    userDict['U_LBC_tf'] = args.U_LBC_tf
    userDict['U_LBC_vo'] = args.U_LBC_vo
    userDict['U_LBC_vf'] = args.U_LBC_vf

    userDict['p_LBC'] = args.p_LBC
    userDict['p_LBC_faces'] = args.p_LBC_faces
    userDict['p_LBC_to'] = args.p_LBC_to
    userDict['p_LBC_tf'] = args.p_LBC_tf
    userDict['p_LBC_vo'] = args.p_LBC_vo
    userDict['p_LBC_vf'] = args.p_LBC_vf

    userDict['turbulence'] = bool(args.turbulence)

    userDict['intensity'] = args.intensity
    userDict['omega'] = args.omega
    userDict['k'] = 10

    return userDict


def userFlags():
    parser = argparse.ArgumentParser(description="A program for generating files for cavitation case")
    parser.add_argument('-n', '--name_case', metavar='', type=str, default='new_case', help="A path to case directory.")
    parser.add_argument('-vtk', '--vtk_path', metavar='', type=str, default='new_case_', help="A path to vtk directory.")
    parser.add_argument('-grid', '--grid_path', metavar='', type=str, default='../polyMesh', help="A path to grid.")
    parser.add_argument('-zero', '--zero_path', metavar='', type=str, default='None', help="A path to zero.")
    parser.add_argument('-output', '--output_path', metavar='', type=str, default='output.txt', help="A path to log.")
    parser.add_argument('-clear', '--clear_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    parser.add_argument('-reconstruct', '--reconstruct_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    programmSettings(parser)
    return parser
