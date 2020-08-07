# Tabuada v3.0
while True:
    print("-" * 30)
    n = int(input("Quer ver a tabuada de qual numero? "))
    print("-" * 30)
    if n < 0:
        break
    else:
        for i in range(1, 11):
            print(f" {n} x {i} = {n * i} ")
print("Programa encerrado!!!".upper())