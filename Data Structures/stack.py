'''
Author: Makson Vinicio

Stack
'''

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def max_element(self):
        try:
            return max(self.items)
        except (TypeError):
            print('Por favor a pilha deve conter somente numeros! ') 
    
    def min_element(self):
        i = 0
        try:
            return min(self.items)
        except (TypeError):
            print('Por favor a pilha deve conter somente numeros! ') 
      

stack = Stack()
#stack.push('hello')
#stack.push('true')
stack.push(4)
stack.push(7)

print(stack.min_element())


print(stack.max_element())

print('-=-' * 10)
while stack.is_empty() != True:
    print(stack.pop())
