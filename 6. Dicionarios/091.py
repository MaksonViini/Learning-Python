# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print("Valores sorteados: ")
for i in range(0, 4):
    jogadores[i] = randint(0, 5)
for k, v in jogadores.items():
    print(f"Jogador {k} tirou {v} no dado ")
    sleep(0.5)
print("-=-" * 15)
print("=== Ranking de jogadores ===".upper())
podio = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for  i, v in enumerate(podio):
    print(f"{i + 1} lugar: {v[0]} com {v[1]}")
    sleep(0.5)
