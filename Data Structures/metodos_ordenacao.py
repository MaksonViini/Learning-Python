class Ordenation:
    def selection_sort(self, lista):
        fim = len(lista)
        for i in range(fim-1):
            # Inicialmente, o menor elemento ja visto e o i-esimo
            posicao_do_menor = i
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_menor]:
                    posicao_do_menor = j

            # Coloca o menor elemento encontrado no inicio da sub-lista
            # Para isso, troca de lugar os elementos da posicao i e da posicao_do_menor
            lista[i], lista[posicao_do_menor] = lista[posicao_do_menor], lista[i]


ini = Ordenation()
lista = [1, 5, 9, 5, 8, 6, 3, 5, 4, 2, 3, 6]
ini.selection_sort(lista)
print(lista)
