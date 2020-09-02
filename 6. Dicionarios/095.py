# Aprimorando os Dicionários
nome = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {nome} fez: '))
gols = ()
s = 0
for i in range (0, partidas):
    gol = int(input(f'Quantos gols {nome} fez no jogo {i+1}: '))
    s += gol
    gols.append(gol)
jogador = {'Nome': nome , 'Partida': partidas , 'Gols': gols, 'Total': s}
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partida"]} partidas')
for c, v in enumerate(jogador['Gols']):
    print(f'=> no {c+1}º jogo ele fez: {v} gols')
print(f'O total de gols foi {s}')