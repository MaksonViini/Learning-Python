# Análise de dados em uma Tupla
tupla = (9, 3, 2, 9)
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
print(f"O valor 3 apareceu na {tupla.index(3) + 1} posicao")
cont = 0
for i in tupla:
    if i % 2 == 0:
        cont += 1
print(f"Os valores pares digitados foram {cont}")