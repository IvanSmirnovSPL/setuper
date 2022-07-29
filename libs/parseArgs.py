
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