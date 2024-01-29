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

def preenche_tabuleiro(esclh, jog):
    if jog == 1:
        if esclh <= 3:
            tabuleiro[0][indexes[0].index(esclh)] = 'x'
        elif esclh <= 6:
            tabuleiro[1][indexes[1].index(esclh)] = 'x'
        else:
            tabuleiro[2][indexes[2].index(esclh)] = 'x'
    elif jog == 2:
        if esclh <= 3:
            tabuleiro[0][indexes[0].index(esclh)] = 'o'
        elif esclh <= 6:
            tabuleiro[1][indexes[1].index(esclh)] = 'o'
        else:
            tabuleiro[2][indexes[2].index(esclh)] = 'o'     

def formata_string():
    string_jogo = ''  
    for line in tabuleiro:
        for ln in line:
            string_jogo += str(ln) + '|'
        string_jogo += '\n-+-+-\n'
    print(string_jogo)

def informa_posicoes_livres():
    livres = ''
    for position in posicoes_livres:
        livres += ', ' + str(position)
    print(f"Posições livres até o momento: {livres}")

def informa_posicoes_ocupadas():
    escolhidas = ''
    for pos in posicoesescolhidas:
        escolhidas += ', ' + str(pos)
    print(f"Posições escolhidas até o momento: {escolhidas}")
    
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

def confere_se_ganhou(jogadas):
    num = 0
    result = True
    while num < 8:
        if jogadas[num] == combinacoes_vencedoras[num]:
            print("É igual")
            result =  False
            break
        num += 1
    print(result)
    return result

resultado = True

while jogadas < 9 and resultado: ## itera até que alguém ganhe ou acabe o jogo.
    for jogador in jogadores: # itera entre os dois jogadores.
        posicao = True # variável para verificar se a posição escolhida no tabuleiro não foi marcada ainda.
        if jogadas <= 8 and resultado: # controla para quando um dos jogadores completar as nove jogadas não seja permitido que o outro jogue.
            while posicao: # verifica se a posição escolhida no tabuleiro está livre.
                escolha = int(input(f"Sua vez de jogar {jogador},\nescolha uma posição vazia: "))
                if escolha not in posicoesescolhidas:
                    posicoesescolhidas.append(escolha)
                    posicoes_livres.remove(escolha)
                    if jogador == jogador1:
                        preenche_tabuleiro(escolha, 1)
                        preenche_jog1(escolha)
                        formata_string()
                        if not confere_se_ganhou(jogadas_jogador1):
                            resultado = False
                            break
                    elif jogador == jogador2:
                        preenche_tabuleiro(escolha, 2)
                        preenche_jog2(escolha)
                        formata_string()
                        if not confere_se_ganhou(jogadas_jogador2):
                            resultado = False
                            break
 #                   formata_string()
                    informa_posicoes_ocupadas()
                    informa_posicoes_livres()
                    posicao = False
                    jogadas += 1
                else:
                    posicao = True
                    print(f"Essa posição já está ocupada {jogador},\nescolha uma das posições abaixo:")
                    print(posicoes_livres)
    
print("Terminou o jogo!")
