# Simulador de Caixa Eletrônico // Forma otimizada
print("=" * 20)
print("       Banco".upper())
print("=" * 20)
valor = float(input("Que valor voce quer sacar? R$"))
cinquenta = valor // 50
dez = (valor % 50) // 10
um = ((valor % 50) % 10) // 1
print(f"{cinquenta:.0f} notas de R$50 ")
print(f"{dez:.0f} notas de R$10 ")
print(f"{um:.0f} notas de R$1 ")