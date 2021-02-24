# Jogo da Adivinhação v2.0
from random import randint
tentativas = 0
n = randint(0, 10)
print("Sou seu computador e pensei em um numero entre 0 e 10 ")
num = int(input("Qual seu palpite? "))
while True:
    tentativas += 1
    if n == num:
        print(f"Voce acertou, eu pensei no numero {n} e voce no {num} ")
        break
    else:
        if n > num:
            print("Mais... Tente outra vez!")
        else:
            print("Menos... Tente outra vez!")
        num = int(input("Qual seu palpite? "))
print(f"Voce acertou com {tentativas} tentativas, Parabens!!!")