# Boletim com listas compostas
info = []
aluno = []
while True:
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    info.append(aluno[:])
    aluno.clear()
    if input("Quer continuar [S/N] ") not in 'Ss': break
print("-=-" * 30)
print(f'{"N°":<3}{"Nome":<14}{"Média":>4}')
c = 0
for i in info:
    print(f"{c:<3}{i[0]:<10}{(i[1] + i[2]) / 2:>4.1f} ")
    c += 1
while True:
    notas = int(input("Mostrar as notas que qual aluno? (999 interrompe): "))
    if notas <= len(info):
        print(f"Notas de {info[notas][0]} sao {[info[notas][1], info[notas][2]]} ")
    elif notas == 999:
        break
    else:
        print("Opcao invalida!!!")