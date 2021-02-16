# Grupo da Maioridade
from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for i in range(1, 5):
    ano = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    if ano_atual - ano >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print(f"Ao todo tivemos {cont_maior} pessoas maiores de idade")
print(f"Ao todo tivemos {cont_menor} pessoas menores de idade")