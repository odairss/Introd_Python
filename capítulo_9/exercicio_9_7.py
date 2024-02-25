"""
Exercício 9.7 - Programa que ler um arquivo-texto e gera um arquivo paginado
onde com cada linha não deve conter mais de 76 caracteres e cada página
pode ter no máximo 60 linhas e no final de cada página tem o número da pág.

pág. 194

"""
lorem_ipsum = open('lorem_ipsum.txt')
lorem_ipsum_paginado = open('lorem_ipsum_paginado.txt','w')
NUM_LINHA = 1
NUM_PAGINA = 1
TAM = 0
SOBRA = ''
for line in lorem_ipsum.readlines():
    if NUM_LINHA > 60:
        NUM_LINHA = 0
        lorem_ipsum_paginado.write('\n')
        lorem_ipsum_paginado.write(f'{NUM_PAGINA}\n\n'.rjust(81,'.'))
        NUM_PAGINA += 1
    else:
        linha_e_sobra = SOBRA+line
        linha_e_sobra = linha_e_sobra.strip()
        if len(linha_e_sobra) == 0:
            lorem_ipsum_paginado.write('{0:>2}'.format(str(NUM_LINHA))+'| '+linha_e_sobra+'\n')
        elif len(linha_e_sobra) > 0 and len(linha_e_sobra) <= 76:
            lorem_ipsum_paginado.write('{0:>2}'.format(str(NUM_LINHA))+'| '+linha_e_sobra+'\n')
        else:
            linha = linha_e_sobra[:76]
            lorem_ipsum_paginado.write('{0:>2}'.format(str(NUM_LINHA))+'| '+linha+'\n')
            TAM = len(linha_e_sobra)
            SOBRA = linha_e_sobra[76:TAM]
    NUM_LINHA += 1

lorem_ipsum.close()
lorem_ipsum_paginado.close()
