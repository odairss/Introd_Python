"""
Exercício 9.2 - Modifica o programa do exercício 9.1 para receber mais
dois parâmetros: a linha de início e a de fim da impressão.
pág. 192

"""
import sys

arg1 = sys.argv[1]

arquivo = open(arg1, 'r')

inicio, fim = sys.argv[2], sys.argv[3]

for linha in arquivo.readlines():
    if linha > inicio and linha < fim:
        print(linha)

arquivo.close()
