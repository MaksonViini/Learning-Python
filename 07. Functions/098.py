# Função de Contador
def contador ():
    for i in range(1, 10, 1):
        print(i, end=' ')
    print('\n','-=-' * 5)
    for i in range(10, 1, -2):
        print(i, end=' ')
    print('\n','-=-' * 5)
    print('Agora e sua vez de personalizar a contagem: ')
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    if inicio > fim:
        passo *= -1
        for i in range(inicio, fim - 1, passo):
            print(i, end=' -> ')
    elif inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' -> ')
    else:
        print("FIM")
    print("FIM")
contador()