# Jogo do Par ou Ímpar
from random import randint
print("-=-" * 15)
print("vamos jogar par ou impar".upper())
print("-=-" * 15)
soma = i = 0
while True:
    pc = randint(0, 10)
    jogador = int(input("Diga um valor: "))
    escolha = str(input("Par ou Impar? [P/I]")).upper()
    soma = jogador + pc
    if soma % 2 == 0:
        print(f"Voce jogou {jogador} e o computador {pc}. Total de {soma} e PAR")
        resultado = 'P'
    else:
        print(f"Voce jogou {jogador} e o computador {pc}. Total de {soma} e IMPAR")
        resultado = 'I'
    if escolha == resultado:
        print("voce Venceu".upper())
        i += 1
    else:
        print("Voce perdeu".upper())
    novamente = str(input("Vamos jogar novamente? [S/N] "))
    if novamente not in 'Ss':
        break
print(f"Voce venceu {i} vezes ")