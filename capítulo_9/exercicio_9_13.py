"""
Exercício 9.13
Programa que recebe 3 parâmetros pela linha de comando, sendo o
nome de um arquivo, a linha inicial e a última linha a ser impressa e imprime
todas as linhas entre a inicial e a final contendo as mesmas.

Pág. 195

"""

import sys

file_name, initial_line, final_line = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

file = open(file_name, 'r')

list_lines = list()

for line in file.readlines():
    list_lines.append(line)

interval = list_lines[initial_line:final_line+1]

for ln in interval:
    print(ln)


file.close()
