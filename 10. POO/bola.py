'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(f'A cor da bola e {self.cor}')

ball = Bola('Azul', 3.5, 'Couro')

ball.troca_cor('Verde')

ball.mostra_cor()
    