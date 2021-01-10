# Custo da Viagem
distancia = int(input("Qual a distancia da viagem em km/h? "))
if distancia <= 200:
    print(f"O valor da viagem e de R$ 0,50 por km e da um total de R$ {0.5 * distancia} ")
else:
    print(f"O valor da viagem acima de 200 km e de R$ 0,45 por km, um total de R$ {0.45 * distancia} ")
