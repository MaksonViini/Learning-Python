# Alistamento Militar
from datetime import date
ano_atual = date.today().year
ano = int(input("Seu ano de nascimento: "))
if (ano_atual - ano) == 18:
    print("Voce deve se alistar")
elif (ano_atual - ano) > 18:
    print("Ja passou do tempo de se alistar")
else:
    print("Ainda vai se alistar")