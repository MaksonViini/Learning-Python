#Aluguel de Carros
dias = int(input("Dias alugados: "))
km = int(input("Km rodados: "))
valor = (dias * 60) + (km * 0.15)
print(f"O total a pagar e de R${valor:.2f} ")