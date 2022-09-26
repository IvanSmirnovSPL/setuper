def fill_decomposeParDict(params):
    return ' numberOfSubdomains {} ; '.format(params['numberOfSubdomains']) + '\n' + \
           ' method          scotch; ' + '\n'

# /*
# 1. Расчёт на одном ядре.
# interPhaseChangeFoam
#
# 2. Расчёт на нескольких ядрах.
# decomposeParDict
# mpirun -np number interPhaseChangeFoam -parallel
# reconstractPar
# */
