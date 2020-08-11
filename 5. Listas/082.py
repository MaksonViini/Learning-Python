# Dividindo valores em várias listas
lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    op = str(input("Quer continuar [S/N] "))
    if op in 'Nn':
        break

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
        
print(f"A lista completa e {lista} ")        
print(f"Pares {pares} ")
print(f"Impares {impares} ")
