"""
Programa que lê duas listas e que gera uma terceira lista
"""
lista1 = []

lista2 = []
x = 0
v = 0

while x < 5:
    elemento = input("digite o elemento %d da primeira lista: " % (x+1))
    lista1.append(elemento)
    x += 1

print("-"*20)

while v < 5:
    item = input("Digite o elemento %d da segunda lista: " % (v+1))
    lista2.append(item)
    v += 1
    
print("-"*20)

lista3 = []
lista3.extend(lista1)
lista3.extend(lista2)
print(lista3)
