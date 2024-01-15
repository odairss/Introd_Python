"""
Exercício 7.5 (pág. 143)

Programa que ler duas strings informadas pelo usuário,
retira da primeira os caracteres que se repetem nas duas
gerando assim, uma terceira string.

"""

string_1 = input("Informe a primeira string: ")
string_2 = input("Informe a segunda string: ")

lista = list()

for char in string_1:
    if char not in string_2:
        lista.append(char)
        
string_3 = ''.join(lista)
print(f"String formada com os caracteres retirados:\n{string_3}")
