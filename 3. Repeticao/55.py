# Maior e menor da sequência
maior = 0
menor = 0
for i in range(1, 4):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    maior = max(maior, peso)
    menor = peso
    menor = min(menor, peso)
print(f"O maior peso e {maior}Kg")
print(f"O menor peso e {menor}Kg")
