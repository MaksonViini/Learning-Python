# Extraindo dados de uma Lista
lista = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    op = str(input("Quer continuar [S/N] "))
    if op in 'Nn':
        break
    if 5 in lista:
        frase = "O valor 5 faz parte da lista"
    else:
        frase = "O valor 5 nao foi encontrado"
lista.sort(reverse=True)
print(f"Voce digitou {len(lista)} elementos ")
print(f"Os valores em ordem decrescente sao {lista} ")
print(frase)
#lista[::-1], outra forma de pegar o final da lista apos ordena-la