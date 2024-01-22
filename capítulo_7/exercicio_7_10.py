"""
Exercício 7.10 da pág. 160.

Um jogo da  velha para dois jogadores.

"""

jogo = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

casasescolhidas = list()

jogadas = 0
jogador = 0

jogador1 = input("Nome do primeiro jogador: ")
jogador2 = input("Nome do segundo jogador: ")

jogadores = [jogador1,jogador2]


while jogadas < 9:

    for jogador in jogadores:
        casavazia = True
        while casavazia:
            casa = int(input(f"Sua vez de jogar {jogador}, escolha uma casa vazia: "))
            if casa not in casasescolhidas:
                casasescolhidas.append(casa)
                casavazia = False
                jogadas += 1
            else:
                casavazia = True
                print(f"Essa casa já está ocupada {jogador},\nescolha outra casa!")
    
print("Terminou o jogo!")

##def jogo_da_velha():
##    
##    linhadesenhada = ''
##    
##    jogo = [[' ',' ',' '],
##            [' ',' ',' '],
##            [' ',' ',' ']]
##    
##    controlador = 0
##        
##    for casas in jogo:
##        
##        linhadesenhada = ''
##        controlador1 = 0
##        
##        for casa in casas:
##            
##            if controlador1 <= 1:
##                linhadesenhada += casa + '|'
##            else:
##                linhadesenhada += casa
##            controlador1 += 1
##            
##        print(linhadesenhada)
##        
##        if controlador <= 1:
##            print("-+-+-")
##        controlador += 1
##        
##
##jogo_da_velha()
