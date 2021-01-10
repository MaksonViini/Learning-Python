# Índice de Massa Corporal
peso = int(input("Entre com seu peso: "))
altura = float(input("Entre com sua altura: "))
imc = peso / altura ** 2
if imc < 18.5:
    print(f"O seu IMC e de {imc:.1f} ")
    print("ABAIXO DO PESO")
elif imc < 25:
    print(f"O seu IMC e de {imc:.1f} ")
    print("PESO IDEAL")
elif imc < 30:
    print(f"O seu IMC e de {imc:.1f} ")
    print("SOBREPESO")
elif imc < 40:
    print(f"O seu IMC e de {imc:.1f} ")
    print("OBESIDADE")
elif imc > 40:
    print(f"O seu IMC e de {imc:.1f} ")
    print("OBESIDADE MORBIDA")