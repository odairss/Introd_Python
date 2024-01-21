"""
Exercício 7.10 da pág. 160.

Um jogo da  velha para dois jogadores.

"""

jogo = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
jogadores = [1,2]

casasescolhidas = list()

jogadas = 0

while jogadas < 9:
    
    jogador = 0
    
    while jogador <= 1:
        
        casa = int(input("escolha uma casa vazia: "))
        if casa not in casasescolhidas:
            casasescolhidas.append(casa)
        else:
            print("Essa casa já está ocupada. Escolha outra casa!")

        jogador += 1
        
    jogadas += 1
    
    if jogadas == 8:
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
