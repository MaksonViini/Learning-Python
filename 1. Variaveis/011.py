#Pintando Parede
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
print(f"Sua parede tem a dimensao de {altura} x {largura} e sua area e de {(altura * largura):.3f} m^2")
print(f"E para pintar essa parede voce precisa de {(altura * largura) / 2:.0f} ")