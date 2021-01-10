# Lista ordenada sem repetições
lista = []
for i in range(5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print("O numero foi adicionado no final da lista ...")
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i, n)
                print(f"O numero foi adicionado na posicao {i} ")
                break
print(lista)        