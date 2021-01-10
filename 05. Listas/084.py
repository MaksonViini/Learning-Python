# Lista composta e análise de dados
pessoas = []
while True:
    nome = str(input("Nome: "))
    peso = str(input("Peso: "))
    pessoas.append([nome, peso])
    if input('Quer continuar? [S/N] ') not in 'Ss': break
print(f"Ao todo voce cadastrou {len(peso)} pessoas")
maior_peso = max([p for n, p in pessoas])
menor_peso = min([p for n, p in pessoas])
print(f"O maior peso foi de {maior_peso}Kg. Peso de {[n for n, p in pessoas if p == maior_peso]} ")
print(f"O menor peso foi de {menor_peso}Kg. Peso de {[n for n, p in pessoas if p == menor_peso]}")
