# Análise de dados do grupo
print("-=-" * 15)
print("cadastre uma pessoa".upper())
print("-=-" * 15)
maior_18 = homens = mulher_com_menos_20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).upper()
    if idade > 18:
        maior_18 += 1
    if sexo in "Mm":
        homens += 1
    elif sexo in "Ff" and idade < 18:
        mulher_com_menos_20 += 1
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        break
print(f"Total de pessoas com mais de 18 anos: {maior_18} ")
print(f"Ao todo temos {homens} homens cadastrados ")
print(f"E temos {mulher_com_menos_20} mulheres com menos de 20 anos cadastradas ")
