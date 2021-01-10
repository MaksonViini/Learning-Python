#Analisador de Textos
nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em MAIUSCULA e {nome.upper()} ")
print(f"Seu nome em minuscula e {nome.lower()} ")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras ")
corte = nome.split()
print(f"Seu primeiro e {corte[0]}, e tem {len(corte[0])} letras")