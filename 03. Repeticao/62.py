# Super Progressão Aritmética v3.0
print("=" * 20)
print("gerador de pa".upper())
print("=" * 20)
termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
cont = 10
i = 0
k = x = 0
while True:
    if i != cont:
        i += 1
        print(termo,"->", end=" ")
        termo += razao
        x += 1
    elif i != 0:
        print("PAUSE".upper())
        termo1 = int(input("\nQuantos termos voce quer mostrar a mais? "))
        cont = termo1
        termo1 += razao
        i = 0
        k += 1
    elif cont == 0:
        break
print(f"Progressao finalizada com {(x + k) - 2} termos ")