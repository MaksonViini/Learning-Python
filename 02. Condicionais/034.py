# Aumentos múltiplos
salario = float(input("Digite seu salario: "))
if salario > 1250:
    print(f"Seu salario e de R$ {salario} e voce teve um aumento de 10%, seu novo salario e de R$ {salario * 1.1:.2f}")
else:
    print(f"Seu salario e de R$ {salario} e voce teve um aumento de 10%, seu novo salario e de R$ {salario * 1.15:.2f}")