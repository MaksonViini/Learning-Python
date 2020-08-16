# Validando entrada de dados em Python
def leia_int (num):
    while True:
        if num.isnumeric():
            return num
            break
        else:
            print("ERRO!, Numero invalido!")
            num = str(input("Digite um numero: "))
n = leia_int(str(input("Digite um numero: ")))
print(f"Voce digitou o numero {n} ")