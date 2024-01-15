"""
Exercício 7.1
Programa que ler duas strings,
verifica se a segunda ocorre dentro da primeira e
imprime o índice.
"""
def find_string():
    string1 = input("Informe a primeira string: ")
    string2 = input("Informe a segunda string: ")
    indice = string1.find(string2)
    if indice > -1:
        print(indice)
