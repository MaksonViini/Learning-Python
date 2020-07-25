#Primeiro e último nome de uma pessoa
nome = str(input("Digite seu nome: ")).strip().split()
print(f"Seu primeiro nome e {nome[0]} ")
print(f"Seu ultimo nome e {nome[-1]} ")