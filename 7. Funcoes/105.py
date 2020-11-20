# Analisando e gerando Dicionários
from statistics import mean
def notas(*notas, sit = False):
    dic = {'Total':len(notas), 'Maior': max(notas), 'Menor': min(notas), 'Media': mean(notas)}
    if sit == True:
        if dic['Media'] < 6:
            dic['Situacao'] = 'Ruim'
        elif dic['Media'] <= 7:
            dic['Situacao'] = 'Razoavel'
        else:
            dic['Situacao'] = 'Boa'
    else:
        return dic
    return dic
print(notas(8, 8, 6, False))