"""
Listagem 7.45 - Jogo da forca (pág. 157)

"""

palavra = input("Digite a palavra secreta: ").lower().strip() # aproveitamos o retorno de input para chamar os métodos de string lower e strip

for x in range(100):
    print() # pulamos várias linhas para que o jogador não veja o que foi digitado como palavra. A ideia é que um jogador escreva uma palavra secreta, e que outro tente descobri-la.
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
        elif erros >= 4:
            linha2 = " \|/ "
            
        print("X%s" % linha2)

        linha3 = ""

        if erros == 5:
            linha3 = "  :\nX /  "
        elif erros >= 6:
            linha3 = "  :\nX / \ "

        print("X%s" % linha3)
        print("X\n===========")

        if erros == 6:
            print("Enforcado!")
            break
