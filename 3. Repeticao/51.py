# Progressão Aritmética
print("=" * 20)
print("10 termos de uma pa".upper())
print("=" * 20)
termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
for i in range(1, 11):
    print(termo,"->", end=" ")
    termo += razao
print("acabou".upper())