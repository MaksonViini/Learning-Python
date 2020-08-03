# Analisador completo
media = 0
mais_velho = 0
cont_M = 0
c = 0
name = 0
for i in range(1, 3):
    c += 1
    print(f"---- {i}ª PESSOA ----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    media += idade
    if sexo in 'Mm': 
        if mais_velho < idade:
            mais_velho = idade
            name = nome
    if sexo in 'Ff':
        cont_M += 1
print(f"A media de idade e {media / c} anos")
print(f"O Homem mais velho tem {mais_velho} anos e se chama {name}")
print(f"Ao todo sao {cont_M} mulheres ")