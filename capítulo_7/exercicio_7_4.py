"""
Exercício 7.4

programa que ler uma string e imprime quantas vezes
cada caractere dessa string aparece nela.

"""

string1 = input("informe uma string qualquer\npara saber quantas vezes\nseus caracteres se repetem: ")

dicionario = {}

for letra in string1:
    if letra not in dicionario:
        if letra != ' ':
            dicionario[letra] = 1
    else:
        dicionario[letra] += 1

for chave, valor in dicionario.items():
    print(f'{chave.upper()}: {valor}x')
    
