#Procurando uma string dentro de outra
nome = str(input("Seu nome completo: ")).strip().upper().split()
print(f"Seu nome tem Ferreira? {'FERREIRA' in nome} ")