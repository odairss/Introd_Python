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
new_file = open('exercicio_9_14.txt', 'w')

list_words = list()

for ln in file.readlines():
    if len(ln) > 1:
        list_words.append(ln.split())

text_cleared = ''

for lista in list_words:
    new_file.write(' '.join(lista))
    new_file.write('\n\n')

file.close()
new_file.close()
