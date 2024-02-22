"""
Exercício 9.1 - Programa que recebe o nome de um
arquivo pela linha de comando e imprime
todas as linhas desse arquivo.
pág. 191.

"""
import sys

nome_do_arquivo = sys.argv[1]

arquivo = open(nome_do_arquivo, 'r')

for linha in arquivo.readlines():
    print(linha)


arquivo.close()
