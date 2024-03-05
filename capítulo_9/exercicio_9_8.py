"""
Exercício 9.8 - Altera o programa do exercício 9.7 da pág. 194
para receber o número de caracteres por linha e o número de linhas por página.

pág. 194
"""
import sys

NUM_PAGINA = 1
NUM = 1
TEXTO = ''

NUM_CHARS = int(sys.argv[1])
NUM_LINES = int(sys.argv[2])

lorem_ipsum = open('lorem_ipsum.txt')
lorem_ipsum_paginado = open('lorem_ipsum_paginado_v2.txt','w')

def numerar_pagina(nome_original):
    global NUM_PAGINA, NUM
    ultima_linha = '\n'
    ultima_linha += f'{NUM_PAGINA}\n'.rjust(81,'.')
    ultima_linha += nome_original + '\n\n'
    NUM_PAGINA += 1
    NUM = 1
    return ultima_linha

def numerar_linha(ln):
    global NUM
    tx = ''
    linha = ln[:NUM_CHARS]
    ln = ln[NUM_CHARS:len(ln)]
    tx = '{0:>2}'.format(str(NUM))+'| '+linha+'\n'
    NUM += 1
    return [tx,ln]

def se_linha_grande(linha_g, nome):
    global TEXTO
    while len(linha_g) > NUM_CHARS:
        if NUM > NUM_LINES:
            TEXTO += numerar_pagina(nome)
        else:
            tx_sbr = numerar_linha(linha_g)
            linha_g = tx_sbr[1]
            TEXTO += tx_sbr[0]
    return [TEXTO, linha_g]

def se_linha_pequena(linha_p, nome):
    global NUM
    tx = ''
    if len(linha_p) <= NUM_CHARS:
        if NUM > NUM_LINES:
            tx = numerar_pagina(nome)
            tx += '{0:>2}'.format(str(NUM))+'| '+linha_p
            NUM += 1
        else:
            tx = '{0:>2}'.format(str(NUM))+'| '+linha_p
            NUM += 1
    return tx

def main():
    global TEXTO
    for line in lorem_ipsum.readlines():
        TEXTO = ''
        result = se_linha_grande(line, lorem_ipsum.name)
        lorem_ipsum_paginado.write(result[0])
        line = result[1]
        lorem_ipsum_paginado.write(se_linha_pequena(line, lorem_ipsum.name))
                
    ultima_linha = '\n'
    ultima_linha += f'{NUM_PAGINA}\n'.rjust(81,'.')
    ultima_linha += lorem_ipsum.name + '\n\n'
    lorem_ipsum_paginado.write(ultima_linha)
    
if __name__ == '__main__':
    main()

lorem_ipsum.close()
lorem_ipsum_paginado.close()
