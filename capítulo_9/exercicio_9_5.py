"""
Exercício 9.5 - Programa que inverte a ordem
das linhas do arquivo pares.txt
pág. 193

"""

pares = open('pares.txt','r+')
uma_lista = list()
for linha in pares.readlines():
    uma_lista.append(int(linha))

uma_lista.reverse()

for n in uma_lista:
    pares.write("%d\n" %n)

pares.close()

