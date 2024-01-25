"""
Exercício 7.10 da pág. 160.

Um jogo da  velha para dois jogadores.

"""

jogo = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

posicoesescolhidas = list()

jogadas = 0
jogador = 0

jogador1 = input("Nome do primeiro jogador: ")
jogador2 = input("Nome do segundo jogador: ")

jogadores = [jogador1,jogador2]


while jogadas < 9: ## itera 9 vezes permitindo que o jogo continue até que não exista mais posições marcadas

    for jogador in jogadores: # itera entre os dois jogadores.
        posicao = True # variável para verificar se a posição escolhida no tabuleiro não foi marcada ainda.
        if jogadas <= 8: # controla para quando um dos jogadores completar as nove jogadas não seja permitido que o outro jogue.
            while posicao: # verifica se a posição escolhida no tabuleiro está livre.
                escolha = int(input(f"Sua vez de jogar {jogador}, escolha uma casa vazia: "))
                if escolha not in posicoesescolhidas:
                    posicoesescolhidas.append(escolha)
                    posicao = False
                    jogadas += 1
                else:
                    posicao = True
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
