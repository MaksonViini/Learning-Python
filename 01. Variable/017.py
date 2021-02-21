#Catetos e Hipotenusa
from math import hypot
cat_ad = float(input("Comprimento do cateto adjacente: "))
cat_op = float(input("Comprimento do cateto oposto: "))
print(f"A hipotenusa vai medir {hypot(cat_ad, cat_op):.2f} ")