# Progressão Aritmética v2.0
print("=" * 20)
print("PRIMEIrOS de uma pa".upper())
print("=" * 20)
termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
i = 0
cont = 10
while i != cont:
    i += 1
    print(termo,"->", end=" ")
    termo += razao
    if i == cont:
        print("PAUSE".upper())
        termo1 = int(input("Quantos termos voce quer mostrar a mais? "))
        cont = termo1
        termo1 += razao
        i = 0
        