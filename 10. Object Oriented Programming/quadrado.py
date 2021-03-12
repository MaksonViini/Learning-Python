'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

'''


class Quadrado:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def muda_valor_lado(self, base, altura):
        self.base = base
        self.altura = altura

    def retorna_valor_lado(self):
        return self.altura

    def calcula_area(self):
        return self.base * self.altura


quad = Quadrado(10, 5)

print(quad.calcula_area())
