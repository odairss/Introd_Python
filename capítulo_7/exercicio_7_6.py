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
lista = list()
char = 0
confirma = True

while num < len(string_1):
    
    if char >= len(string_3):
        char = 0
        
    confirma = True
    for letra in string_2:
        if letra == string_1[num]:
            lista.append(string_3[char])
            char += 1
            confirma = False
            
    if confirma:
        lista.append(string_1[num])
    num += 1

resultado = ''.join(lista)
print(resultado)
