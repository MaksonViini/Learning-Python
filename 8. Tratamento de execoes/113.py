def leia_float ():
    while True:
        try:
            num = float(input('Digite um numero real: ').replace(',', '.'))
        except (ValueError, TypeError):
            print('Por favor, digite um numero real valido! ')
        else:
            return num
def leia_int ():
    while True:
        try:
            num = int(input('Digite um numero inteiro valido: '))
        except (ValueError, TypeError):
            print('Por favor digite um numero inteiro valido! ')    
        else:
            return num 
n1 = leia_int()
n2 = leia_float()
print(f'O numero inteiro digitado foi {n1} e o real {n2} ')
