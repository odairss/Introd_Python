"""
Listagem 7.45 - Jogo da forca (pág. 157)

linha2 = ["  |  ", " \| ", " \|/ "]
linha3 = ["  |  "]
linha4= [" /  ", " / \ "]
linhas = [linha2, linha3, linha4]

"""

# palavra = input("Digite a palavra secreta: ").lower().strip() 

palavras = ["pato", 'artesanato','sapato','marketing','piloto',
            'ganso', 'smartphone', 'notebook', 'cadeira', 'geladeira'
            'girafa', 'escritório', 'suplemento', 'academia', 'astronauta'
            'elefante', 'fuselagem', 'bicicleta', 'armagedom', 'medicina'
            'porco', 'química', 'astronomia', 'astrologia', 'Júpiter'
            'cachorro', 'universo', 'universal', 'universitário', 'universidade'
            'gato', 'gatuno', 'felino', 'proteína', 'carboidrato', 'aminoácidos']


for x in range(100):
    linha2 = list("X     ")
    linha3 = list("X     ")
    linha4 = list("X     ")
    numero = int(input("Informe um número: "))
    indice = (numero * 776) % len(palavras)
    print() # pulamos várias linhas para que o jogador não veja o que foi digitado como palavra. A ideia é que um jogador escreva uma palavra secreta, e que outro tente descobri-la.
    digitadas = []
    acertos = []
    erros = 0
    while True:
        senha = ""
        for letra in palavras[indice].lower():
            senha += letra if letra in acertos else "." # decidir o valor a retornar, dependendo de uma condição.
        print(senha)

        if senha == palavras[indice]:
            print("Você acertou!")
            break
        tentativa = input("\nDigite uma letra: ").lower().strip()
        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue # ignorar todas as linhas até o fim da repetição e voltar para o início, sem terminá-la.
        else:
            digitadas += tentativa
            if tentativa in palavras[indice]:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
        print("X==:==\nX  :  ")
        print("X  0  " if erros >= 1 else "X")

            
        if erros == 2:
            linha2[3] = "|"
        elif erros == 3:
            linha2[2] = "\\"
        elif erros == 4:
            linha2[4] = "/"
            
        print("".join(linha2))


        if erros == 5:
            linha3[3] = "|"

        print("".join(linha3))
        
        
        if erros == 6:
            linha4[2] = "/"
            
        if erros >= 7:
            linha4[4] = "\\"

        print("".join(linha4))
        print("X\n===========")

        if erros == 7:
            print(f"Enforcado!\nA palavra secreta é: {palavras[indice].lower()}")
            break
