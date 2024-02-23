"""
Exercício 9.4 - Programa que recebe o nome de dois arquivos pela linha de comando
e gera novo arquivo com as linhas do primeiro e segundo arquivo.
pág. 193

"""

import sys

param1 = sys.argv[1]
param2 = sys.argv[2]

pares = open(param1,'r')
impares = open(param2,'r')

paresimpares = open('par_impar.txt','w')

lista = list()

for l in pares.readlines():
    lista.append(int(l))

for l in impares.readlines():
    lista.append(int(l))

lista.sort()

for n in lista:
    paresimpares.write('%d\n' % n)
    
pares.close()
impares.close()
paresimpares.close()
    
