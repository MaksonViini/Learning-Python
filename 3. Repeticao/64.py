# Tratando vários valores v1.0
n = soma = cont = 0
while n != 999:
    n = int(input("Digite um numero [999 para parar]: "))
    if n < 999:
        soma += n
        cont += 1
print(f"Voce digitou {cont} numeros, e a soma deles foram de {soma} ")
