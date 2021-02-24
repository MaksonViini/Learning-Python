# Cadastro de Jogador de Futebol
jogador = {'Nome': str(input("Nome do jogador: ")), "Gols": []}
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for v in range(0, partidas):
    jogador['Gols'].append(int(input(f"     Quantos gols na partida {v}? ")))
jogador['Total'] = sum(jogador['Gols'])
print('-=-' * 15)
print(jogador)
print('-=-' * 15)
print(f"O campo nome tem o valor {jogador['Nome']}")
print(f"O campo gols tem o valor {jogador['Gols']}")
print(f"O campo total tem o valor {jogador['Total']}")
for i in range(0, partidas):
    print(f"    => Na partida {i}, fez {jogador['Gols'][i]} ")
print(f"Foi um total de {jogador['Total']} gols ")