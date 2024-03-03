"""
Exercício 9.7 - Programa que ler um arquivo-texto e gera um arquivo paginado
onde com cada linha não deve conter mais de 76 caracteres e cada página
pode ter no máximo 60 linhas e no final de cada página tem o número da pág.

pág. 194

"""

NUM_PAGINA = 1
TAMANHO = 0
NUM = 1

lorem_ipsum = open('lorem_ipsum.txt')
lorem_ipsum_paginado = open('lorem_ipsum_paginado.txt','w')

def main():
    global NUM, TAMANHO, NUM_PAGINA
    for line in lorem_ipsum.readlines():
        TAMANHO = len(line)
        while len(line) > 76:
            if NUM > 60:
                ultima_linha = '\n'
                ultima_linha += f'{NUM_PAGINA}\n\n'.rjust(81,'.')
                lorem_ipsum_paginado.write(ultima_linha)
                NUM_PAGINA += 1
                NUM = 1
            else:
                linha = line[:76]
                line = line[76:TAMANHO]
                TAMANHO = len(line)
                lorem_ipsum_paginado.write('{0:>2}'.format(str(NUM))+'| '+linha+'\n')
                NUM += 1      
            
        if len(line) <= 76:
            if NUM > 60:
                ultima_linha = '\n'
                ultima_linha += f'{NUM_PAGINA}\n\n'.rjust(81,'.')
                lorem_ipsum_paginado.write(ultima_linha)
                NUM_PAGINA += 1
                NUM = 1
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
