# Palpites para a Mega Sena
from random import sample
print("-" * 30)
print("       jogar na mega sena".upper())
print("-" * 30)
total = []
lista = []
jogos = int(input("Quantos jogos voce quer sortear? "))
print(f"-=-=-Sorteando {jogos} jogos-=-=-".upper())
for i in range(0, jogos):
    lista.append(sample(range(1, 60), 6))
total.append(lista)
for i in range(0, jogos):
    print(f"\nJogo {i + 1}: {total[0][i]}")
print("boa sorte!!!".upper())