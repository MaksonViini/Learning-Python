# Números primos
num = int(input("Digite um numero: "))
cont = sum(num % i == 0 for i in range(1, num + 1))
if cont == 2:
    print(f"O numero {num} e primo, pois e divisivel {cont} vezes ")
else:
    print(f"O numero {num} nao e primo, pois e divisivel {cont} vezes")