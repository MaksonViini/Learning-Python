# Unindo dicionários e listas
dic = {'Nome': '', 'Sexo': '', 'Idade': ''}
#dic = {'Nome': str(input('Nome: ')), 'Sexo': str(input('Sexo: ')), 'Idade': int(input('Idade: '))}
lista = []
while True:
    dic['Nome'] =  str(input('Nome: ')),
    dic['Sexo'] =  str(input('Sexo: '))
    if dic['Sexo'] not in 'MmFf':
        print('ERRO! Por favor digite somente M ou F')
        Sexo =  str(input('Sexo: '))
    dic['Idade'] =  int(input('Idade: '))
    lista.append(dic)
    op = str(input('Quer continuar ? [S/N]: '))
    if op in 'Nn':
        break
    else:
        print('ERRO! Por favor digite somente S ou N')
        op = str(input('Quer continuar ? [S/N]: '))
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas: ')
print(f'B) A media de idade e {sum(lista[1]) /(len(lista))}: ')
#print(f'C) Ao todo temos {len(lista)} pessoas cadastradas: ')
#print(f'D) Ao todo temos {len(lista)} pessoas cadastradas: ')
print(dic)

