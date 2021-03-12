'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. 
Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''


class Retangulo:
    def __init__(self, lado_A, lado_B):
        self.lado_A = lado_A
        self.lado_B = lado_B

    def muda_valor(self, new_lado_A, new_lado_B):
        self.lado_A = new_lado_A
        self.lado_B = new_lado_B

    def retorna_valor(self):
        return self.lado_A, self.lado_B

    def area(self):
        return self.lado_A * self.lado_B

    def perimetro(self):
        return self.lado_A + self.lado_B


a = float(input("Entre com um numeros: "))
b = float(input("Entre com um numeros: "))

retangulo = Retangulo(a, b)

print(retangulo.retorna_valor())
print(retangulo.area())
print(retangulo.perimetro())
