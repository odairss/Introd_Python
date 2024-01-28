"""
Exercício 7.10 da pág. 160.

Um jogo da  velha para dois jogadores.

"""
jogador1 = input("Nome do primeiro jogador: ")
jogador2 = input("Nome do segundo jogador: ")

indexes = [[1,2,3], [4,5,6], [7,8,9]]
tabuleiro = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

combinacoes_vencedoras = [[3,6,9],[2,5,8],[1,4,7],[4,5,6],[1,2,3],[1,5,9],[7,8,9],[3,5,7]]

jogadas_jogador1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

jogadas_jogador2 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

posicoesescolhidas = list()

jogadas = 0
jogador = 0


jogadores = [jogador1,jogador2]

posicoes_livres = list(range(1,10))

def preenche_jog1(valor):
    num = 0
    while num < 8:
        if valor in combinacoes_vencedoras[num]:
            indexe = combinacoes_vencedoras[num].index(valor)
            jogadas_jogador1[num][indexe] = valor
        num += 1

def preenche_jog2(valor):
    num = 0
    while num < 8:
        if valor in combinacoes_vencedoras[num]:
            indexe = combinacoes_vencedoras[num].index(valor)
            jogadas_jogador2[num][indexe] = valor
        num += 1

while jogadas < 9: ## itera 9 vezes permitindo que o jogo continue até que não exista mais posições marcadas

    for jogador in jogadores: # itera entre os dois jogadores.
        posicao = True # variável para verificar se a posição escolhida no tabuleiro não foi marcada ainda.
        if jogadas <= 8: # controla para quando um dos jogadores completar as nove jogadas não seja permitido que o outro jogue.
            while posicao: # verifica se a posição escolhida no tabuleiro está livre.
                escolha = int(input(f"Sua vez de jogar {jogador},\nescolha uma posição vazia: "))
                if escolha not in posicoesescolhidas:
                    posicoesescolhidas.append(escolha)
                    posicoes_livres.remove(escolha)
                    
                    if jogador == jogador1:
                        preenche_jog1(escolha)
                        if escolha <= 3:
                            tabuleiro[0][indexes[0].index(escolha)] = 'x'
                        elif escolha <= 6:
                            tabuleiro[1][indexes[1].index(escolha)] = 'x'
                        else:
                            tabuleiro[2][indexes[2].index(escolha)] = 'x'
                            
                    elif jogador == jogador2:
                        preenche_jog2(escolha)
                        if escolha <= 3:
                            tabuleiro[0][indexes[0].index(escolha)] = 'o'
                        elif escolha <= 6:
                            tabuleiro[1][indexes[1].index(escolha)] = 'o'
                        else:
                            tabuleiro[2][indexes[2].index(escolha)] = 'o'
                            
                    string_jogo = ''    
                    for line in tabuleiro:
                        for ln in line:
                            string_jogo += str(ln) + '|'
                        string_jogo += '\n-+-+-\n'
                    print(string_jogo)

                    escolhidas = ''
                    for pos in posicoesescolhidas:
                        escolhidas += ', ' + str(pos)
                    print(f"Posições escolhidas até o momento: {escolhidas}")

                    livres = ''
                    for position in posicoes_livres:
                        livres += ', ' + str(position)
                    print(f"Posições livres até o momento: {livres}")
                    posicao = False
                    jogadas += 1
                else:
                    posicao = True
                    print(f"Essa posição já está ocupada {jogador},\nescolha uma das posições abaixo:")
                    print(posicoes_livres)
    
print("Terminou o jogo!")
