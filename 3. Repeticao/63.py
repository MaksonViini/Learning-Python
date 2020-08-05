# Sequência de Fibonacci v1.0
print("-" * 40)
print("Sequencia de Fibonacci")
print("-" * 40)
n = int(input("Quantos termos voce quer mostrar? "))
fibonacci = 0
f = 1
while n != 0:
    print(f"{fibonacci} -> ", end= " ")
    fibonacci = fibonacci + f
    f = fibonacci - f
    n -= 1
print("Acabou")