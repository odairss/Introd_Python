"""
Exercício 9.14
Programa que ler um arquivo-texto e elimina os espaços repetidos entre
as palavras e no fim das linhas. O arquivo de saída também não tem
mais de uma linha em branco repetida.
Pág. 195

"""

import sys

file_name = sys.argv[1]

file = open(file_name, 'r')

list_words = list()

for ln in file.readlines():
    if len(ln) > 1:
        list_words.append(ln.split())

text_cleared = ''

for lista in list_words:
    text_cleared += ' '.join(lista)
    text_cleared += '\n'

print(text_cleared)
file.close()
