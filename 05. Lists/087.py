# Mais sobre Matriz em Python
matriz = [[], [], []]
par = terceira = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Digite um valor para [{i}, {j}] ")))
        if matriz[i][j] % 2 == 0: par += matriz[i][j]
        if j == 2: terceira += matriz[i][j]
print('=' * 30)
print(f"Matriz resultante\n{matriz[0]}\n{matriz[1]}\n{matriz[2]} ")
print('=' * 30)
print(f"A soma dos valores pares e {par}")
print(f"A soma dos valores da terceira coluna e {terceira}")
print(f"O maior valor da segunda linha e {max(matriz[1])} ")