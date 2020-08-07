# Maior e Menor valores
n = soma = i = 0
lista = []
op = 's'
while op in 'Ss':
    n = int(input("Digite um numero: "))
    soma += n
    lista.append(n)
    i += 1 
    op = str(input("Quer continuar? [S/N] "))
print(f"Voce digitou {i} numeros e a media foi {soma / i} ")
print(f"O maior valor digitado foi {max(lista)} e o menor foi {min(lista)} ")