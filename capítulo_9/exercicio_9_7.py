"""
Exercício 9.7 - Programa que ler um arquivo-texto e gera um arquivo paginado
onde com cada linha não deve conter mais de 76 caracteres e cada página
pode ter no máximo 60 linhas e no final de cada página tem o número da pág.

pág. 194

"""
arquivo_original = open('texto_qualquer.txt')
nun_linha = 1
num_pagina = 1
tam = 0
sobra = ''
for line in arquivo_original.readlines():
    line = line+sobra
    if len(line) <= 76:
        print(str(nun_linha)+' '+line)
    else:
        tam = len(line)
        linha = line.slice[:76]
        print(str(nun_linha)+' '+linha)
        sobra = line.slice[76:tam]
    num_linha += 1
