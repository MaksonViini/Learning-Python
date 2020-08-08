# Estatísticas em produtos
print("-=-" * 15)
print("Lojas".upper())
print("-=-" * 15)
lista = []
nome = []
i = 0
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco: R$"))
    nome.append(produto)
    lista.append(preco)
    op = str(input("Quer continuar? [S/N] "))
    if op in 'Nn':
        break
    if preco > 1000:
        i += 1
print("-" * 7, "Fim do programa".upper(), "-" * 7)
print(f"O total da compra foi R${sum(lista)} ")
print(f"Temos {i} produto custando mais que R$1000.00")
print(f"O produto mais barato foi {nome[lista.index(min(lista))]} que custa R${min(lista)} ")
