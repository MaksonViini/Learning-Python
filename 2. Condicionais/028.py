#Jogo da Adivinhação v.1.0
from random import randint
from time import sleep
print("-=-" * 15)
pc = randint(0, 5)
num = int(input("Em que numero pensei? "))
print("-=-" * 15)
sleep(1)
if pc == num:
    print(f"Parabens !!!, eu pensei no numero {pc} e vc no {num} ")
else:
    print(f"Infelizmente nao foi dessa vez, pensei no {pc} e vc no {num}, tente novamente... !!!")