#Sorteando uma ordem na lista
from random import shuffle
aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundi aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f"A ordem e ...")
print(lista)