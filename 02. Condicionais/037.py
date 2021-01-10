# Conversor de Bases Numéricas
num = int(input("Informe um valor para conversao: "))
op = int(input("Escolha [1] para binaria, [2] octal, [3] decimal "))
if op == 1:
    print(f"O numero {num} em binario e {bin(num)[2:]}")
elif op == 2:
    print(f"O numero {num} em octal e {oct(num)[2:]}")
elif op == 3:
    print(f"O numero {num} em hexadecimal e {hex(num)[2:]}")
else:
    print("Opcao invalida")