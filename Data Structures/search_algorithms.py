'''
Author: Makson Vinicio

Algoritmos de busca
'''


class Search:
    def binary_seach(self, lista, element):
        left, right = 0, len(lista) - 1
        while left <= right:
            middle = (left + right) // 2
            if lista[middle] == element:
                return middle
            elif lista[middle] > element:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def sequential(self, lista, element):
        for i in range(len(lista)):
            if lista[i] == element:
                return i
        return False


t = Search()

print(t.binary_seach([1, 2, 3, 4, 5, 6], 4))

print(t.sequential([1, 2, 3, 4, 5, 6], 4))
