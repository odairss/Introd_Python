"""
Exercício 9.12 - Modifica o programa da questão 9.11 para registrar a linha e a coluna de cada ocorrência da palavra no arquivo.

pág. 195

"""

import sys
from exercicio_9_12_componentes import dict_factory

name_file = sys.argv[1]

file = open(name_file)

def main():
    dict_factory(file)

if __name__ == '__main__':
    main()
    
file.close()


