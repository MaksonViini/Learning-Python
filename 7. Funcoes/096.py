# Função que calcula área
print("Controle de terreno")
print("-" * 20)
def area (c, l):
    print(f"A area de um terreno de {c:.2f} x {l:.2f} e de {c * l}m ")
c = float(input("Comprimento:(m) "))
l = float(input("Largura:(m) "))
area(c, l)