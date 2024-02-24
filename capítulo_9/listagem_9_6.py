"""
Listagem 9.6 - Processamento de um arquivo
pág. 194

"""

LARGURA = 79

entrada = open('entrada.txt','r')

for linha in entrada.readlines():
    if linha[0] == ';':
        continue
    elif linha[0] == '>':
        print(linha[1:].rjust(LARGURA))
    elif linha[0] == '*':
        print(linha[1:].center(LARGURA))
    else:
        print(linha)

entrada.close()
