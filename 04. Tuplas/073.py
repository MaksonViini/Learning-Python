# Tuplas com Times de Futebol
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f"Os 5 primeiros times sao: {times[0: 5]}")
print(f"Os ultimos colocados sao: {times[-4:]} ")
print(f"Os times em ordem sao: {sorted(times)}")
print(f"O time da Chapecoence esta na posicao {times.index('Chapecoense')}")