# Cadastro de Trabalhador em Python
from datetime import date
ano = date.today().year
trabalhador = {'Nome': str(input("Nome: ")), 'Idade': ano - int(input("Ano de nascimento: ")), 
'Carteira': int(input("Carteira de trabalho (0 nao tem): "))}
if trabalhador['Carteira'] != 0:
    trabalhador['Ano contratacao'] = int(input("Ano de contratacao: "))
    trabalhador['Salario'] = float(input("Salario: R$"))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Ano contratacao'] + 35) - ano)
for k, v in trabalhador.items():
    print(f"{k} tem o valor de {v} ")