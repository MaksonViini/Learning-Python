# Soma ímpares múltiplos de três
soma = 0
x = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        x += 1
        soma += i
print(f"A soma dos {x} valores e {soma} ")