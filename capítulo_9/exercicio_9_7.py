"""
Exercício 9.7 - Programa que ler um arquivo-texto e gera um arquivo paginado
onde com cada linha não deve conter mais de 76 caracteres e cada página
pode ter no máximo 60 linhas e no final de cada página tem o número da pág.

pág. 194

"""

NUM_PAGINA = 1
NUM = 1
TEXTO = ''

lorem_ipsum = open('lorem_ipsum.txt')
lorem_ipsum_paginado = open('lorem_ipsum_paginado.txt','w')

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
    linha = ln[:76]
    ln = ln[76:len(ln)]
    tx = '{0:>2}'.format(str(NUM))+'| '+linha+'\n'
    NUM += 1
    return [tx,ln]

def se_linha_grande(linha_g, nome):
    global TEXTO
    while len(linha_g) > 76:
        if NUM > 60:
            TEXTO += numerar_pagina(nome)
        else:
            tx_sbr = numerar_linha(linha_g)
            linha_g = tx_sbr[1]
            TEXTO += tx_sbr[0]
    return [TEXTO, linha_g]

def se_linha_pequena(linha_p, nome):
    global NUM
    tx = ''
    if len(linha_p) <= 76:
        if NUM > 60:
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
