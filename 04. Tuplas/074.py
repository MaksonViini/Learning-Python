# Maior e menor valores em Tupla
from random import sample
tupla = tuple(sample(range(10), 5))
print(tupla)
print(f"O maior valor e {max(tupla)} e o menor e {min(tupla)} ")