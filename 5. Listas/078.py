# Maior e Menor valores na Lista
from random import sample
lista = []
lista = (sample(range(10), 10))
print(lista)
print(f"O maior  e {max(lista)} na posicao {lista.index(max(lista)) + 1}, o menor e {min(lista)} na posicao {lista.index(min(lista)) + 1} ")