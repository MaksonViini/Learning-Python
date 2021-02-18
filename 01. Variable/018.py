#Seno, Cosseno e Tangente
from math import sin, cos, tan, radians
angulo = float(input("Informe o angulo: "))
print(f"O SENO do angulo de {angulo} e de {sin(radians(angulo)):.2f} ")
print(f"O COSSENO do angulo de {angulo} e de {cos(radians(angulo)):.2f} ")
print(f"A TANGENTE do angulo de {angulo} e de {tan(radians(angulo)):.2f} ")