# Unindo dicionários e listas
dic = {'Nome': '', 'Sexo': '', 'Idade': ''}
lista = []
idade = []
while True:
    dic['Nome'] =  str(input('Nome: ')),
    dic['Sexo'] =  str(input('Sexo: '))
    if dic['Sexo'] not in 'MmFf':
        print('ERRO! Por favor digite somente M ou F')
        Sexo =  str(input('Sexo: '))
    dic['Idade'] =  int(input('Idade: '))
    idade.append(dic['Idade'])
    lista.append(dic)
    op = str(input('Quer continuar ? [S/N]: '))
    if op in 'Nn':
        break
    elif op not in 'NnSs':
        print('ERRO! Por favor digite somente S ou N')
        op = str(input('Quer continuar ? [S/N]: '))
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas: ')
media = sum(idade) / (len(idade))
print(f'B) A media de idade e {media}: ')
print(f'C) As mulheres cadastradas foram: ')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(p['Nome'], end = '')
print()
print(lista[0])
print(f'C) Lista das pessoas que estao com idade acima da media: ')
for p in lista:
    if p['Idade'] > media:
        print(p['Idade'], end = ' ')
print()