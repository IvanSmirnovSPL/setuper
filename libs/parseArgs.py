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
        elif key == 'compressible_fluxScheme':
            files_data['system']['fvSchemes']['compressible_fluxScheme'] = str(userDict[key])
        elif key == 'ddtSchemes_default':
            files_data['system']['fvSchemes']['ddtSchemes_default'] = str(userDict[key])
        elif key == 'ddtSchemes_fluxIntegrator':
            files_data['system']['fvSchemes']['ddtSchemes_fluxIntegrator'] = str(userDict[key])
        elif key == 'gradSchemes_default':
            files_data['system']['fvSchemes']['gradSchemes_default'] = str(userDict[key])
        elif key == 'divSchemes_default':
            files_data['system']['fvSchemes']['divSchemes_default'] = str(userDict[key])
        elif key == 'divSchemes_div_tauMC_':
            files_data['system']['fvSchemes']['divSchemes_div_tauMC_'] = str(userDict[key])
        elif key == 'divSchemes_div_S_U_':
            files_data['system']['fvSchemes']['divSchemes_div_S&U_'] = str(userDict[key])
        elif key == 'laplacianSchemes_default':
            files_data['system']['fvSchemes']['laplacianSchemes_default'] = str(userDict[key])
        elif key == 'interpolationSchemes_default':
            files_data['system']['fvSchemes']['interpolationSchemes_default'] = str(userDict[key])
        elif key == 'interpolationSchemes_scheme':
            files_data['system']['fvSchemes']['interpolationSchemes_scheme'] = str(userDict[key])
        elif key == 'interpolationSchemes_reconstruct_thermorho_':
            files_data['system']['fvSchemes']['interpolationSchemes_reconstruct_thermorho_'] = str(userDict[key])
        elif key == 'interpolationSchemes_reconstruct_rhoU_':
            files_data['system']['fvSchemes']['interpolationSchemes_reconstruct_rhoU_'] = str(userDict[key])
        elif key == 'interpolationSchemes_reconstruct_rhoE_':
            files_data['system']['fvSchemes']['interpolationSchemes_reconstruct_rhoE_'] = str(userDict[key])
        elif key == 'snGradSchemes_default':
            files_data['system']['fvSchemes']['snGradSchemes_default'] = str(userDict[key])
        elif key == 'pointSync':
            files_data['system']['createPatchDict']['pointSync'] = str(userDict[key])
        elif key == 'name':
            files_data['constant']['thermophysicalProperties']['name'] = str(userDict[key])
        elif key == 'type':
            files_data['constant']['thermophysicalProperties']['type'] = str(userDict[key])
        elif key == 'constructFrom':
            files_data['system']['extrudeMeshDict']['constructFrom'] = str(userDict[key])
        elif key == 'set':
            files_data['system']['createPatchDict']['set'] = str(userDict[key])
        elif key == 'action':
            files_data['system']['topoSetDict']['action'] = str(userDict[key])
        elif key == 'source':
            files_data['system']['topoSetDict']['source'] = str(userDict[key])
        elif key == 'patch':
            files_data['system']['topoSetDict']['patch'] = str(userDict[key])
        elif key == 'box':
            files_data['system']['topoSetDict']['box'] = str(userDict[key])
        elif key == 'numberOfSubdomains':
            files_data['system']['decomposeParDict']['numberOfSubdomains'] = str(userDict[key])
        elif key == 'method':
            files_data['system']['decomposeParDict']['method'] = str(userDict[key])
        elif key == 'sourceCase':
            files_data['system']['extrudeMeshDict']['sourceCase'] = str(userDict[key])
        elif key == 'sourcePatches':
            files_data['system']['extrudeMeshDict']['sourcePatches'] = str(userDict[key])
        elif key == 'exposedPatchName':
            files_data['system']['extrudeMeshDict']['exposedPatchName'] = str(userDict[key])
        elif key == 'flipNormals':
            files_data['system']['extrudeMeshDict']['flipNormals'] = str(userDict[key])
        elif key == 'extrudeModel':
            files_data['system']['extrudeMeshDict']['extrudeModel'] = str(userDict[key])
        elif key == 'nLayers':
            files_data['system']['extrudeMeshDict']['nLayers'] = str(userDict[key])
        elif key == 'expansionRatio':
            files_data['system']['extrudeMeshDict']['expansionRatio'] = str(userDict[key])
        elif key == 'thickness':
            files_data['system']['extrudeMeshDict']['thickness'] = str(userDict[key])
        elif key == 'mergeFaces':
            files_data['system']['extrudeMeshDict']['mergeFaces'] = str(userDict[key])
        elif key == 'mergeTol':
            files_data['system']['extrudeMeshDict']['mergeTol'] = str(userDict[key])
        elif key == 'E_solver':
            files_data['system']['fvSolution']['E_solver'] = str(userDict[key])
        elif key == 'E_preconditioner':
            files_data['system']['fvSolution']['E_preconditioner'] = str(userDict[key])
        elif key == 'E_tolerance':
            files_data['system']['fvSolution']['E_tolerance'] = str(userDict[key])
        elif key == 'E_relTol':
            files_data['system']['fvSolution']['E_relTol'] = str(userDict[key])
        elif key == 'U_solver':
            files_data['system']['fvSolution']['U_solver'] = str(userDict[key])
        elif key == 'U_preconditioner':
            files_data['system']['fvSolution']['U_preconditioner'] = str(userDict[key])
        elif key == 'U_tolerance':
            files_data['system']['fvSolution']['U_tolerance'] = str(userDict[key])
        elif key == 'U_relTol':
            files_data['system']['fvSolution']['U_relTol'] = str(userDict[key])
        elif key == 'SIMPLE_nNonOrthogonalCorrectors':
            files_data['system']['fvSolution']['SIMPLE_nNonOrthogonalCorrectors'] = str(userDict[key])
        elif key == 'BoundaryType':
            files_data['constant']['boundaryRegion']['BoundaryType'] = str(userDict[key])
        elif key == 'Label':
            files_data['constant']['cellTable']['Label'] = str(userDict[key])
        elif key == 'BoundaryIndex':
            files_data['constant']['boundaryRegion']['BoundaryIndex'] = str(userDict[key])
        elif key == 'size':
            files_data['constant']['boundaryRegion']['size'] = str(userDict[key])
        elif key == 'MaterialType':
            files_data['constant']['cellTable']['MaterialType'] = str(userDict[key])
        elif key == 'MaterialId':
            files_data['constant']['cellTable']['MaterialId'] = str(userDict[key])
        elif key == 'GroupId':
            files_data['constant']['cellTable']['GroupId'] = str(userDict[key])
        elif key == 'simulationType':
            files_data['constant']['turbulenceProperties']['simulationType'] = str(userDict[key])
        elif key == 'phases':
            files_data['constant']['thermophysicalProperties']['phases'] = str(userDict[key])
        elif key == 'properties_rhoe':
            files_data['constant']['thermophysicalProperties']['properties_rhoe'] = str(userDict[key])
        elif key == 'properties_TP':
            files_data['constant']['thermophysicalProperties']['properties_TP'] = str(userDict[key])
        elif key == 'properties_TRho':
            files_data['constant']['thermophysicalProperties']['properties_TRho'] = str(userDict[key])
        elif key == 'mixture_calculation_method':
            files_data['constant']['thermophysicalProperties']['mixture_calculation_method'] = str(userDict[key])
        elif key == 'value':
            files_data['constant']['g']['value'] = str(userDict[key])


def programmSettings(parser):
    parser.add_argument('-application', '--application', metavar='', type=str, default='laplacianMesh', help='')
    parser.add_argument('-startFrom', '--startFrom', metavar='', type=str, default='startTime', help='')
    parser.add_argument('-startTime', '--startTime', metavar='', type=str, default='0', help='')
    parser.add_argument('-stopAt', '--stopAt', metavar='', type=str, default='endTime', help='')
    parser.add_argument('-endTime', '--endTime', metavar='', type=str, default='300', help='')
    parser.add_argument('-deltaT', '--deltaT', metavar='', type=str, default='1e-8', help='')
    parser.add_argument('-writeControl', '--writeControl', metavar='', type=str, default='timeStep', help='')
    parser.add_argument('-writeInterval', '--writeInterval', metavar='', type=str, default='10', help='')
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
    parser.add_argument('-compressible_fluxScheme', '--compressible_fluxScheme', metavar='', type=str,
                        default='AUSMPlusUp', help='')
    parser.add_argument('-ddtSchemes_default', '--ddtSchemes_default', metavar='', type=str, default='Euler', help='')
    parser.add_argument('-ddtSchemes_fluxIntegrator', '--ddtSchemes_fluxIntegrator', metavar='', type=str,
                        default='Euler', help='')
    parser.add_argument('-gradSchemes_default', '--gradSchemes_default', metavar='', type=str, default='linear',
                        help='')
    parser.add_argument('-divSchemes_default', '--divSchemes_default', metavar='', type=str, default='none', help='')
    parser.add_argument('-divSchemes_div_tauMC_', '--divSchemes_div_tauMC_', metavar='', type=str, default='linear',
                        help='')
    parser.add_argument('-divSchemes_div_S_U_', '--divSchemes_div_S_U_', metavar='', type=str, default='linear',
                        help='')
    parser.add_argument('-laplacianSchemes_default', '--laplacianSchemes_default', metavar='', type=str,
                        default='corrected', help='')
    parser.add_argument('-interpolationSchemes_default', '--interpolationSchemes_default', metavar='', type=str,
                        default='linear', help='')
    parser.add_argument('-interpolationSchemes_scheme', '--interpolationSchemes_scheme', metavar='', type=str,
                        default='upwind', help='')
    parser.add_argument('-interpolationSchemes_reconstruct_thermorho_', '--interpolationSchemes_reconstruct_thermorho_',
                        metavar='', type=str, default='$scheme', help='')
    parser.add_argument('-interpolationSchemes_reconstruct_rhoU_', '--interpolationSchemes_reconstruct_rhoU_',
                        metavar='', type=str, default='$scheme', help='')
    parser.add_argument('-interpolationSchemes_reconstruct_rhoE_', '--interpolationSchemes_reconstruct_rhoE_',
                        metavar='', type=str, default='$scheme', help='')
    parser.add_argument('-snGradSchemes_default', '--snGradSchemes_default', metavar='', type=str, default='corrected',
                        help='')
    parser.add_argument('-pointSync', '--pointSync', metavar='', type=str, default='false', help='')
    parser.add_argument('-name', '--name', metavar='', type=str, default='alphav', help='')
    parser.add_argument('-type', '--type', metavar='', type=str, default='AlphavTRho', help='')
    parser.add_argument('-constructFrom', '--constructFrom', metavar='', type=str, default='surface', help='')
    parser.add_argument('-set', '--set', metavar='', type=str, default='symmetry', help='')
    parser.add_argument('-action', '--action', metavar='', type=str, default='subtract', help='')
    parser.add_argument('-source', '--source', metavar='', type=str, default='boxToFace', help='')
    parser.add_argument('-patch', '--patch', metavar='', type=str, default='Symmetry', help='')
    parser.add_argument('-box', '--box', metavar='', type=str, default='1e6 1e6 0', help='')
    parser.add_argument('-numberOfSubdomains', '--numberOfSubdomains', metavar='', type=str, default='8', help='')
    parser.add_argument('-method', '--method', metavar='', type=str, default='scotch', help='')
    parser.add_argument('-sourceCase', '--sourceCase', metavar='', type=str, default='"<case>"', help='')
    parser.add_argument('-sourcePatches', '--sourcePatches', metavar='', type=str, default='(sym)', help='')
    parser.add_argument('-exposedPatchName', '--exposedPatchName', metavar='', type=str, default='sym', help='')
    parser.add_argument('-flipNormals', '--flipNormals', metavar='', type=str, default='false', help='')
    parser.add_argument('-extrudeModel', '--extrudeModel', metavar='', type=str, default='offsetSurface', help='')
    parser.add_argument('-nLayers', '--nLayers', metavar='', type=str, default='1', help='')
    parser.add_argument('-expansionRatio', '--expansionRatio', metavar='', type=str, default='1.0', help='')
    parser.add_argument('-thickness', '--thickness', metavar='', type=str, default='0.05', help='')
    parser.add_argument('-mergeFaces', '--mergeFaces', metavar='', type=str, default='false', help='')
    parser.add_argument('-mergeTol', '--mergeTol', metavar='', type=str, default='0', help='')
    parser.add_argument('-E_solver', '--E_solver', metavar='', type=str, default='PCG', help='')
    parser.add_argument('-E_preconditioner', '--E_preconditioner', metavar='', type=str, default='DIC', help='')
    parser.add_argument('-E_tolerance', '--E_tolerance', metavar='', type=str, default='1e-06', help='')
    parser.add_argument('-E_relTol', '--E_relTol', metavar='', type=str, default='0', help='')
    parser.add_argument('-U_solver', '--U_solver', metavar='', type=str, default='PCG', help='')
    parser.add_argument('-U_preconditioner', '--U_preconditioner', metavar='', type=str, default='DIC', help='')
    parser.add_argument('-U_tolerance', '--U_tolerance', metavar='', type=str, default='1e-06', help='')
    parser.add_argument('-U_relTol', '--U_relTol', metavar='', type=str, default='0', help='')
    parser.add_argument('-SIMPLE_nNonOrthogonalCorrectors', '--SIMPLE_nNonOrthogonalCorrectors', metavar='', type=str,
                        default='2', help='')
    parser.add_argument('-BoundaryType', '--BoundaryType', metavar='', type=str, default='outlet', help='')
    parser.add_argument('-Label', '--Label', metavar='', type=str, default='Region_1', help='')
    parser.add_argument('-BoundaryIndex', '--BoundaryIndex', metavar='', type=str, default='5', help='')
    parser.add_argument('-size', '--size', metavar='', type=str, default='2174', help='')
    parser.add_argument('-MaterialType', '--MaterialType', metavar='', type=str, default='fluid', help='')
    parser.add_argument('-MaterialId', '--MaterialId', metavar='', type=str, default='2', help='')
    parser.add_argument('-GroupId', '--GroupId', metavar='', type=str, default='1', help='')
    parser.add_argument('-simulationType', '--simulationType', metavar='', type=str, default='laminar', help='')
    parser.add_argument('-phases', '--phases', metavar='', type=str, default='vapour liquid', help='')
    parser.add_argument('-properties_rhoe', '--properties_rhoe', metavar='', type=str,
                        default='vapor_mass_fraction temperature pressure speed_of_sound viscosity thermal_conductivity',
                        help='')
    parser.add_argument('-properties_TP', '--properties_TP', metavar='', type=str,
                        default='vapor_mass_fraction density internal_energy speed_of_sound viscosity thermal_conductivity',
                        help='')
    parser.add_argument('-properties_TRho', '--properties_TRho', metavar='', type=str,
                        default='(vapor_volume_fraction)', help='')
    parser.add_argument('-mixture_calculation_method', '--mixture_calculation_method', metavar='', type=str,
                        default='volume_average', help='')
    parser.add_argument('-value', '--value', metavar='', type=str, default='0 0 0', help='')


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
    userDict['compressible_fluxScheme'] = args.compressible_fluxScheme
    userDict['ddtSchemes_default'] = args.ddtSchemes_default
    userDict['ddtSchemes_fluxIntegrator'] = args.ddtSchemes_fluxIntegrator
    userDict['gradSchemes_default'] = args.gradSchemes_default
    userDict['divSchemes_default'] = args.divSchemes_default
    userDict['divSchemes_div_tauMC_'] = args.divSchemes_div_tauMC_
    userDict['divSchemes_div_S_U_'] = args.divSchemes_div_S_U_
    userDict['laplacianSchemes_default'] = args.laplacianSchemes_default
    userDict['interpolationSchemes_default'] = args.interpolationSchemes_default
    userDict['interpolationSchemes_scheme'] = args.interpolationSchemes_scheme
    userDict['interpolationSchemes_reconstruct_thermorho_'] = args.interpolationSchemes_reconstruct_thermorho_
    userDict['interpolationSchemes_reconstruct_rhoU_'] = args.interpolationSchemes_reconstruct_rhoU_
    userDict['interpolationSchemes_reconstruct_rhoE_'] = args.interpolationSchemes_reconstruct_rhoE_
    userDict['snGradSchemes_default'] = args.snGradSchemes_default
    userDict['pointSync'] = args.pointSync
    userDict['name'] = args.name
    userDict['type'] = args.type
    userDict['constructFrom'] = args.constructFrom
    userDict['set'] = args.set
    userDict['action'] = args.action
    userDict['source'] = args.source
    userDict['patch'] = args.patch
    userDict['box'] = '(' + unpackArg(args.box) + ')'
    userDict['numberOfSubdomains'] = args.numberOfSubdomains
    userDict['method'] = args.method
    userDict['sourceCase'] = args.sourceCase
    userDict['sourcePatches'] = args.sourcePatches
    userDict['exposedPatchName'] = args.exposedPatchName
    userDict['flipNormals'] = args.flipNormals
    userDict['extrudeModel'] = args.extrudeModel
    userDict['nLayers'] = args.nLayers
    userDict['expansionRatio'] = args.expansionRatio
    userDict['thickness'] = args.thickness
    userDict['mergeFaces'] = args.mergeFaces
    userDict['mergeTol'] = args.mergeTol
    userDict['E_solver'] = args.E_solver
    userDict['E_preconditioner'] = args.E_preconditioner
    userDict['E_tolerance'] = args.E_tolerance
    userDict['E_relTol'] = args.E_relTol
    userDict['U_solver'] = args.U_solver
    userDict['U_preconditioner'] = args.U_preconditioner
    userDict['U_tolerance'] = args.U_tolerance
    userDict['U_relTol'] = args.U_relTol
    userDict['SIMPLE_nNonOrthogonalCorrectors'] = args.SIMPLE_nNonOrthogonalCorrectors
    userDict['BoundaryType'] = args.BoundaryType
    userDict['Label'] = args.Label
    userDict['BoundaryIndex'] = args.BoundaryIndex
    userDict['size'] = args.size
    userDict['MaterialType'] = args.MaterialType
    userDict['MaterialId'] = args.MaterialId
    userDict['GroupId'] = args.GroupId
    userDict['simulationType'] = args.simulationType
    userDict['phases'] = '(' + unpackArg(args.phases) + ')'
    userDict['properties_rhoe'] = '(' + unpackArg(args.properties_rhoe) + ')'
    userDict['properties_TP'] = '(' + unpackArg(args.properties_TP) + ')'
    userDict['properties_TRho'] = args.properties_TRho
    userDict['mixture_calculation_method'] = args.mixture_calculation_method
    userDict['value'] = '(' + unpackArg(args.value) + ')'
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
