# Sistema interativo de ajuda em Python
from time import sleep
def ajuda (texto):
    print(f'Acessando o manual do comando {texto} ')
    sleep(0.5)
    help(texto)

while True:
    print('--' * 12)
    print(' Sistema de ajuda PyHelp')
    print('--' * 12)
    f = str(input("Funcao ou Biblioteca > "))
    if f in 'FIMfim':
        break
    else:
        ajuda(f)
