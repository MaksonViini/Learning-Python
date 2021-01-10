# Analisando Triângulos v2.0
print("-=-" * 10)
print("analisador de triangulos".upper())
print("-=-" * 10)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 != r2 and r2 != r3 and r1 != r3:
        print("Os seguimentos PODEM FORMAR um triangulo ESCALENO")
    elif r1 == r2 and r2 == r3 and r1 == r3:
        print("Os seguimentos PODEM FORMAR um triangulo EQUILATERO")
    else:
        print("Os seguimentos PODEM FORMAR um triangulo ISOCELES")
else:
    print("Os seguimentos NAO PODEM FORMAR um triangulo")