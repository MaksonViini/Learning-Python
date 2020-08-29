import codecs
arquivo = codecs.open('arq15.txt', mode='w+', encoding='utf-8')
print('-=-' * 30)
while True:
    string = input('BODY: ').replace('"', '').replace('\n', ' ')
    body = string.split(' ')
    for i in body:
        arquivo.write(f'{i} ')
    arquivo.write('\n')
    print()
    op = str(input('Continuar? '))
    if op in 'Nn':
        break
arquivo.close()