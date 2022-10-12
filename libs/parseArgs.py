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
        if key == 'libs':
            files_data['system']['controlDict']['libs'] = str(userDict[key])
        elif key == 'np':
            files_data['system']['decomposeParDict']['numberOfSubdomains'] = str(userDict[key])
        elif key == 'application':
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
        elif key == 'fluxScheme':
            files_data['system']['fvSchemes']['fluxScheme'] = str(userDict[key])
        elif key == 'ddtSchemes':
            files_data['system']['fvSchemes']['ddtSchemes'] = str(userDict[key])
        elif key == 'fluxIntegrator':
            files_data['system']['fvSchemes']['fluxIntegrator'] = str(userDict[key])
        elif key == 'gradSchemes':
            files_data['system']['fvSchemes']['gradSchemes'] = str(userDict[key])
        elif key == 'divSchemes':
            files_data['system']['fvSchemes']['divSchemes'] = str(userDict[key])
        elif key == 'div_tauMC':
            files_data['system']['fvSchemes']['div_tauMC'] = str(userDict[key])
        elif key == 'laplacianSchemes':
            files_data['system']['fvSchemes']['laplacianSchemes'] = str(userDict[key])
        elif key == 'interpolationSchemes':
            files_data['system']['fvSchemes']['interpolationSchemes'] = str(userDict[key])
        elif key == 'reconstruct_U':
            files_data['system']['fvSchemes']['reconstruct_U'] = str(userDict[key])
        elif key == 'reconstruct_p':
            files_data['system']['fvSchemes']['reconstruct_p'] = str(userDict[key])
        elif key == 'reconstruct_thermo':
            files_data['system']['fvSchemes']['reconstruct_thermo'] = str(userDict[key])
        elif key == 'snGradSchemes':
            files_data['system']['fvSchemes']['snGradSchemes'] = str(userDict[key])
        elif key == 'solver':
            files_data['system']['fvSolution']['solver'] = str(userDict[key])
        elif key == 'U_solver':
            files_data['system']['fvSolution']['U_solver'] = str(userDict[key])
        elif key == 'smoother':
            files_data['system']['fvSolution']['smoother'] = str(userDict[key])
        elif key == 'nSweeps':
            files_data['system']['fvSolution']['nSweeps'] = str(userDict[key])
        elif key == 'tolerance':
            files_data['system']['fvSolution']['tolerance'] = str(userDict[key])
        elif key == 'relTol':
            files_data['system']['fvSolution']['relTol'] = str(userDict[key])
            files_data['constant']['thermophysicalProperties']['relTol'] = str(userDict[key])
        elif key == 'U':
            files_data['system']['fvSolution']['U'] = str(userDict[key])
        elif key == 'simulationType':
            files_data['constant']['turbulenceProperties']['simulationType'] = str(userDict[key])
        elif key == 'phases':
            files_data['constant']['thermophysicalProperties']['phases'] = str(userDict[key])
        elif key == 'Tmin':
            files_data['constant']['thermophysicalProperties']['Tmin'] = str(userDict[key])
        elif key == 'Tmax':
            files_data['constant']['thermophysicalProperties']['Tmax'] = str(userDict[key])
        elif key == 'maxIter':
            files_data['constant']['thermophysicalProperties']['maxIter'] = str(userDict[key])
        elif key == 'logPSatFile':
            files_data['constant']['thermophysicalProperties']['logPSatFile'] = str(userDict[key])
        elif key == 'TSatFile':
            files_data['constant']['thermophysicalProperties']['TSatFile'] = str(userDict[key])
        elif key == 'rho1SatFile':
            files_data['constant']['thermophysicalProperties']['rho1SatFile'] = str(userDict[key])
        elif key == 'rho2SatFile':
            files_data['constant']['thermophysicalProperties']['rho2SatFile'] = str(userDict[key])
        elif key == 'rho1SatDerFile':
            files_data['constant']['thermophysicalProperties']['rho1SatDerFile'] = str(userDict[key])
        elif key == 'rho2SatDerFile':
            files_data['constant']['thermophysicalProperties']['rho2SatDerFile'] = str(userDict[key])
        elif key == 'gvFile':
            files_data['constant']['thermophysicalProperties']['gvFile'] = str(userDict[key])
        elif key == 'glFile':
            files_data['constant']['thermophysicalProperties']['glFile'] = str(userDict[key])
        elif key == 'TstepFile':
            files_data['constant']['thermophysicalProperties']['TstepFile'] = str(userDict[key])
        elif key == 'g':
            files_data['constant']['g']['g'] = str(userDict[key])


def programmSettings(parser):
    parser.add_argument('-libs', '--libs', metavar='', type=str, default='libWENOEXT.so', help='')
    parser.add_argument('-np', '--np', metavar='', type=str, default='1', help="Number of processes.")
    parser.add_argument('-application', '--application', metavar='', type=str, default='FAKTFoam', help='')
    parser.add_argument('-startFrom', '--startFrom', metavar='', type=str, default='startTime', help='')
    parser.add_argument('-startTime', '--startTime', metavar='', type=str, default='0', help='')
    parser.add_argument('-stopAt', '--stopAt', metavar='', type=str, default='endTime', help='')
    parser.add_argument('-endTime', '--endTime', metavar='', type=str, default='1e-3', help='')
    parser.add_argument('-deltaT', '--deltaT', metavar='', type=str, default='1e-07', help='')
    parser.add_argument('-writeControl', '--writeControl', metavar='', type=str, default='adjustable', help='')
    parser.add_argument('-writeInterval', '--writeInterval', metavar='', type=str, default='1e-5', help='')
    parser.add_argument('-purgeWrite', '--purgeWrite', metavar='', type=str, default='0', help='')
    parser.add_argument('-writeFormat', '--writeFormat', metavar='', type=str, default='ascii', help='')
    parser.add_argument('-writePrecision', '--writePrecision', metavar='', type=str, default='6', help='')
    parser.add_argument('-writeCompression', '--writeCompression', metavar='', type=str, default='off', help='')
    parser.add_argument('-timeFormat', '--timeFormat', metavar='', type=str, default='general', help='')
    parser.add_argument('-timePrecision', '--timePrecision', metavar='', type=str, default='6', help='')
    parser.add_argument('-runTimeModifiable', '--runTimeModifiable', metavar='', type=str, default='true', help='')
    parser.add_argument('-adjustTimeStep', '--adjustTimeStep', metavar='', type=str, default='yes', help='')
    parser.add_argument('-maxCo', '--maxCo', metavar='', type=str, default='0.1', help='')
    parser.add_argument('-maxDeltaT', '--maxDeltaT', metavar='', type=str, default='1', help='')
    parser.add_argument('-fluxScheme', '--fluxScheme', metavar='', type=str, default='AUSMPlusUp', help='')
    parser.add_argument('-ddtSchemes', '--ddtSchemes', metavar='', type=str, default='Euler', help='')
    parser.add_argument('-fluxIntegrator', '--fluxIntegrator', metavar='', type=str, default='RK45', help='')
    parser.add_argument('-gradSchemes', '--gradSchemes', metavar='', type=str, default='linear', help='')
    parser.add_argument('-divSchemes', '--divSchemes', metavar='', type=str, default='none', help='')
    parser.add_argument('-div_tauMC', '--div_tauMC', metavar='', type=str, default='WENOUpwindFit_3_0', help='')
    parser.add_argument('-laplacianSchemes', '--laplacianSchemes', metavar='', type=str, default='linear_corrected',
                        help='')
    parser.add_argument('-interpolationSchemes', '--interpolationSchemes', metavar='', type=str, default='linear',
                        help='')
    parser.add_argument('-reconstruct_U', '--reconstruct_U', metavar='', type=str, default='upwind', help='')
    parser.add_argument('-reconstruct_p', '--reconstruct_p', metavar='', type=str, default='upwind', help='')
    parser.add_argument('-reconstruct_thermo', '--reconstruct_thermo', metavar='', type=str, default='upwind', help='')
    parser.add_argument('-snGradSchemes', '--snGradSchemes', metavar='', type=str, default='corrected', help='')
    parser.add_argument('-solver', '--solver', metavar='', type=str, default='diagonal', help='')
    parser.add_argument('-U_solver', '--U_solver', metavar='', type=str, default='smoothSolver', help='')
    parser.add_argument('-smoother', '--smoother', metavar='', type=str, default='GaussSeidel', help='')
    parser.add_argument('-nSweeps', '--nSweeps', metavar='', type=str, default='2', help='')
    parser.add_argument('-tolerance', '--tolerance', metavar='', type=str, default='1e-09', help='')
    parser.add_argument('-relTol', '--relTol', metavar='', type=str, default='1e-5', help='')
    parser.add_argument('-U', '--U', metavar='', type=str, default='$U', help='')
    parser.add_argument('-simulationType', '--simulationType', metavar='', type=str, default='laminar', help='')
    parser.add_argument('-phases', '--phases', metavar='', type=str, default='vapour_liquid', help='')
    parser.add_argument('-g', '--g', metavar='', type=str, default=' 0_9.81_0', help='')

def dictFromUserFlags(args):
    userDict = {}
    userDict['libs'] = args.libs
    userDict['np'] = args.np
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
    userDict['fluxScheme'] = args.fluxScheme
    userDict['ddtSchemes'] = args.ddtSchemes
    userDict['fluxIntegrator'] = args.fluxIntegrator
    userDict['gradSchemes'] = args.gradSchemes
    userDict['divSchemes'] = args.divSchemes
    userDict['div_tauMC'] = unpackArg(args.div_tauMC)
    userDict['laplacianSchemes'] = unpackArg(args.laplacianSchemes)
    userDict['interpolationSchemes'] = args.interpolationSchemes
    userDict['reconstruct_U'] = args.reconstruct_U
    userDict['reconstruct_p'] = args.reconstruct_p
    userDict['reconstruct_thermo'] = args.reconstruct_thermo
    userDict['snGradSchemes'] = args.snGradSchemes
    userDict['solver'] = args.solver
    userDict['U_solver'] = args.U_solver
    userDict['smoother'] = args.smoother
    userDict['nSweeps'] = args.nSweeps
    userDict['tolerance'] = args.tolerance
    userDict['relTol'] = args.relTol
    userDict['U'] = args.U
    userDict['simulationType'] = args.simulationType
    userDict['phases'] = unpackArg(args.phases)
    userDict['g'] = unpackArg(args.g)

    return userDict


def userFlags():
    parser = argparse.ArgumentParser(description="A program for generating files for cavitation case")
    parser.add_argument('-n', '--name_case', metavar='', type=str, default='new_case', help="A path to case directory.")
    parser.add_argument('-vtk', '--vtk_path', metavar='', type=str, default='new_case_', help="A path to vtk directory.")
    parser.add_argument('-grid', '--grid_path', metavar='', type=str, default='../polyMesh', help="A path to grid.")
    parser.add_argument('-table', '--table_path', metavar='', type=str, default='/opt/kpvm/ismirnov/bin/tables', help="A path to table.")
    parser.add_argument('-zero', '--zero_path', metavar='', type=str, default='None', help="A path to zero.")
    parser.add_argument('-output', '--output_path', metavar='', type=str, default='output.txt', help="A path to log.")
    parser.add_argument('-clear', '--clear_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    parser.add_argument('-reconstruct', '--reconstruct_case_path', metavar='', type=str, default=None,
                        help="A path to case directory, which is necessary to clear.")
    programmSettings(parser)
    return parser
