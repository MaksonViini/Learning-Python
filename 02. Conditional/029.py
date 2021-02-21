#Radar eletrônico
velocidade = int(input("Entre com sua velocidade atual em Km/h: "))
if velocidade >= 80:
    print("VOCE FOI MULTADO !!")
    print(f"Voce excedeu o limite de 80Km/h em {velocidade - 80}Km/h e foi multado em R$ {(velocidade - 80) * 7} ")
else:
    print("Boa Viagem !!!")
