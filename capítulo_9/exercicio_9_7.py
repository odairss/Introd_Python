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

def numerar_pagina():
    global NUM_PAGINA, NUM
    ultima_linha = '\n'
    ultima_linha += f'{NUM_PAGINA}\n\n'.rjust(81,'.')
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

##def configurar_pagina(linha):
##    global TEXTO
##    if len(linha) > 76:
##        if NUM > 60:
##            TEXTO += numerar_pagina()
##        else:
##            tx_sbr = numerar_linha(linha)
##            linha = tx_sbr[1]
##            TEXTO += tx_sbr[0]
##        configurar_pagina(linha)
##    return [TEXTO, linha]

def main():
    global NUM
    for line in lorem_ipsum.readlines():
        while len(line) > 76:
            if NUM > 60:
                lorem_ipsum_paginado.write(numerar_pagina())
            else:
                tx_sbr = numerar_linha(line)
                line = tx_sbr[1]
                lorem_ipsum_paginado.write(tx_sbr[0])    
            
        if len(line) <= 76:
            if NUM > 60:
                lorem_ipsum_paginado.write(numerar_pagina())
                lorem_ipsum_paginado.write('{0:>2}'.format(str(NUM))+'| '+line)
                NUM += 1
            else:
                lorem_ipsum_paginado.write('{0:>2}'.format(str(NUM))+'| '+line)
                NUM += 1
                
    ultima_linha = '\n'
    ultima_linha += f'{NUM_PAGINA}\n\n'.rjust(81,'.')
    lorem_ipsum_paginado.write(ultima_linha)
    
if __name__ == '__main__':
    main()

lorem_ipsum.close()
lorem_ipsum_paginado.close()
