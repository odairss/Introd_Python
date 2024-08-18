"""
Exercício 9.15
Altera o programa Jogo da Forca da pág. 185 utilizando um arquivo texto
com as palavras a serem carregadas na lista de palavras e gera outro arquivo
com o número de acertos dos cinco melhores jogadores.

Pág. 195

"""
import random

palavras_gravadas = open('exercicio_9_15.txt','r')

palavras = list()

for word in palavras_gravadas.readlines():
    palavras.append(word.strip())


lista_com_um = random.sample(range(0,56),1)
palavra = palavras[lista_com_um[0]].lower()

for x in range(100):
    digitadas = []
    acertos = []
    erros = 0
    while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else "." # decidir o valor a retornar, dependendo de uma condição.
        print(senha)

        if senha == palavra:
            print("Você acertou!")
            lista_com_um = random.sample(range(0,56),1)
            palavra = palavras[lista_com_um[0]].lower()
            digitadas = []
            acertos = []
            erros = 0
            break
        
        tentativa = input("\nDigite uma letra: ").lower().strip()
        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue # ignorar todas as linhas até o fim da repetição e voltar para o início, sem terminá-la.
        else:
            digitadas += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
        print("X==:==\nX  :  ")
        print("X  0  " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " \| "
        elif erros == 4:
            linha2 = " \|/ "
            
        print("X%s" % linha2)

        linha3 = ""

        if erros == 5:
            linha3 = " /  "
        elif erros >= 6:
            linha3 = " / \ "

        print("X%s" % linha3)
        print("X\n===========")

        if erros == 6:
            print("Enforcado!")
            lista_com_um = random.sample(range(0,56),1)
            palavra = palavras[lista_com_um[0]].lower()
            digitadas = []
            acertos = []
            erros = 0
            break

palavras_gravadas.close()
