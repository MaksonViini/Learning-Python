# Número por Extenso
extenso = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 
'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 
'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input("Digite um numero entre 0 e 20: "))
while num not in range(0, 21):
    num = int(input("Digite um numero entre 0 e 20: "))
print(f"O numero {num} por extenso e {extenso[num].capitalize()} ")