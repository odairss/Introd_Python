"""
Exercício 9.3 - Programa que ler os arquivos pares.txt e ímpares.txt
e gera o arquivo paresimpares.txt preservando a ordem númerica.
pág. 193

"""
pares = open('pares.txt','r')
impares = open('ímpares.txt','r')
paresimpares = open('paresimpares.txt','w')

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
    
