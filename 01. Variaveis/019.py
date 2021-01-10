#Sorteando um item na lista
from random import choice
aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundi aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
selecionado = choice(lista)
print(f"O aluno escolhido foi {selecionado} ")
