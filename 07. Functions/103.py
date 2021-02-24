# Ficha do Jogador
def jogador (nome, gols):
    if nome == '':
        nome = "<Desconhecido>"
    if gols == '' or not gols.isnumeric():
        gols = 0
    return f"O jogador {nome} fez {gols} gols no campeonato "
print(jogador(str(input("Nome do jogador: ")).strip(), str(input("Gols: ")).strip()))
