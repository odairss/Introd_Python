"""
Exercício 9.11 - Programa que ler um arquivo e cria um dicionário
onde cada palavra do arquivo é uma chave no dicionário cujo valor, é a quantidade
de ocorrências dessa palavra no arquivo.

pág. 195

"""

import sys
from exercicio_9_11_componentes import dict_factory

name_file = sys.argv[1]

file = open(name_file)

def main():
    dict_factory(file)

if __name__ == '__main__':
    main()
    
file.close()


