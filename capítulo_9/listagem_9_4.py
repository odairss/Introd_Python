"""
Listagem 9.4 - Gravação de números pares e ímpares em arquivos diferentes
pág. 192

"""

impares = open('ímpares.txt', 'w')
pares = open('pares.txt', 'w')

for n in range(0,1001):
    if n % 2 == 0:
        pares.write('%d\n' % n)
    else:
        impares.write('%d\n' % n)

impares.close()
pares.close()
