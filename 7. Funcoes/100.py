# Funções para sortear e somar
from random import sample
def sortear ():
    lista = []
    lista = sample(range(10), 5)
    return lista
def somar_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma
sorteio = sortear()
print(f'Sorteando 5 valores na lista: {sorteio} PRONTO!')
print(f"Somando os valores pares de  {sorteio}, temos {somar_par(sorteio)} ")