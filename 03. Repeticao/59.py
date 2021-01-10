# Criando um Menu de Opções
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
while True:
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NUMEROS")
    print("[5] SAIR")
    op = int(input(">>>>>>>>> Qual sua opcao? "))
    if op == 1:
        print(f"A soma entre {n1} + {n2} = {n1 + n2} ")
    elif op == 2:
        print(f"A multiplicacao entre {n1} x {n2} = {n1 * n2} ")
    elif op == 3:
        print(f"O maior entre {n1} e {n2} e {max(n1, n2)} ")
    elif op == 4:
        print("-=- Entre com novos numeros -=-")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif op == 5:
        break
    else:
        continue