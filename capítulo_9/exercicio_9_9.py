"""
Exercício 9.9 - Programa que recebe uma lista de nomes de arquivo
e os imprime, um por um.

pág. 194

"""
import sys
from exercicio_9_9_componentes import *

files_names = sys.argv[1:]
    
def main():
   lista_de_arquivos = adicionar_arquivos_em_lista(files_names)
   imprimir_arquivos(lista_de_arquivos)
   fechar_arquivos(lista_de_arquivos)


if __name__ == '__main__':
    main()
