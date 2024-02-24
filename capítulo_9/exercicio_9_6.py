"""
Exercício 9.6 - Modifica o programa da Listagem  9.6 imprimindo 40 vezes
o símbolo de = se este for o primeiro caractere da linha e adiciona também
a opção de imprimir até que se pressione Enter cada vez que uma linha
iniciar com . como primeiro caractere
pág. 194

"""
from pynput.keyboard import keyboard, Listener

LARGURA = 79
def processando_arquivos():
    entrada = open('entrada.txt','r')

    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == '*':
            print(linha[1:].center(LARGURA))

        elif linha[0] == '=':
            print(linha[0]*39+linha)
        elif linha[0] == '.':
            enter = input()
        else:
            print(linha)

    entrada.close()

if __name__ == '__main__':
    processando_arquivos()
