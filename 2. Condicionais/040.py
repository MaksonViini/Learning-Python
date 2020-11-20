# Aquele clássico da Média
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print(f"A media do aluno e {media}")
if media >= 6:
    print("Aprovado!!!")
else:
    print("Reprovado")