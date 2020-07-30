# Ano Bissexto
from datetime import date
ano = int(input("Quer analisar qual ano? Digite 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} e bissexto")
    else:
        print(f"O ano {ano} nao e bissexto ")
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} e bissexto")
    else:
        print(f"O ano {ano} nao e bissexto ")
