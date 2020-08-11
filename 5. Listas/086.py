# Matriz em Python
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Digite um valor para [{i}, {j}] ")))
print(f"Matriz resultante\n{matriz[0]:^5}\n{matriz[1]:^5}\n{matriz[2]:^5} ")