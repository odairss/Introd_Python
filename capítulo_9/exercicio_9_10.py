"""
Exercício 9.10 - Programa que recebe uma lista de nomes de arquivos
e gera apenas um grande arquivo de saída.

pág. 194

"""

import sys
from exercicio_9_10_componentes import *


def main():
    nomes = sys.argv[1:]
    write_files_in_big_file(nomes)
    

if __name__ == '__main__':
    main()
