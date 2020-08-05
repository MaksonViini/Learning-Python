# Cálculo do Fatorial
#from math import factorial
num = int(input("Digite um numero: "))
cont = 1
#print(f"Fatorial de {num} = {factorial(num)} ")
while num != 1:
    cont *= num
    num -= 1
    print(num+1 ,"x", end=" ")
print(f"1 = {cont}")

