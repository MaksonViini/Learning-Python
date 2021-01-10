# Classificando Atletas
from datetime import date
ano_atual = date.today().year
ano = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano
if idade <= 9:
    print(f"O atleta tem {idade} anos")
    print("Classificacao: Mirim")
elif idade <= 14:
    print(f"O atleta tem {idade} anos")
    print("Classificacao: Infatil")
elif idade <= 19:
    print(f"O atleta tem {idade} anos")
    print("Classificacao: Junior")
elif idade <= 25:
    print(f"O atleta tem {idade} anos")
    print("Classificacao: Senior")
else:
    print(f"O atleta tem {idade} anos")
    print("Classificacao: Master")