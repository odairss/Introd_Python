"""
Exercício 7.6

Programa que ler três strings e
substitui pelos caracteres da terceira
aqueles que se repetem na primeira e na segunda.

"""

string_1 = input("Informe a primeira string: ")
string_2 = input("Informe a segunda string: ")
string_3 = input("Informe a terceira string: ")

num = 0
num1 = 0
lista = list()

while num < len(string_1):
    while num1 < len(string_2):
        if string_1[num] == string_2[num1]:
            lista.append(string_3[num1])
        else:
            lista.append(string_1[num])
        num1 += 1
    num += 1

resultado = ''.join(lista)
print(resultado)
