# Valores únicos em uma Lista
lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    if lista.count(n) == 2:
        print("Valor duplicado! Nao vai ser adicionado")
        lista.pop()
    else:
        print("Valor adicionado com sucesso: ")
    op = str(input("Quer continuar [S/N] "))
    if op in 'Nn':
        break
print(sorted(lista))