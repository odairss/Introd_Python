indexes = [[1,2,3], [4,5,6], [7,8,9]]
tabuleiro = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

combinacoes_vencedoras = [[3,6,9],[2,5,8],[1,4,7],[4,5,6],[1,2,3],[1,5,9],[7,8,9],[3,5,7]]

jogadas_jogador1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

jogadas_jogador2 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

posicoesescolhidas = list()


posicoes_livres = list(range(1,10))

def preenche_tabuleiro(esclh, jog):
    global tabuleiro
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
        string_jogo = string_jogo.rstrip('|')
        string_jogo += '\n-+-+-\n'
    string_jogo = string_jogo[0:29].upper()
    print(string_jogo)

def informa_posicoes_livres():
    livres = ''
    for position in posicoes_livres:
        livres += ', ' + str(position)
    print(f"Posições livres até o momento: {livres}")
    print(":".rjust(50,':'))

def informa_posicoes_ocupadas():
    escolhidas = ''
    for pos in posicoesescolhidas:
        escolhidas += ', ' + str(pos)
    print(f"Posições escolhidas até o momento: {escolhidas}")
    
def preenche_jog1(valor):
    global jogadas_jogador1
    num = 0
    while num < 8:
        if valor in combinacoes_vencedoras[num]:
            indexe = combinacoes_vencedoras[num].index(valor)
            jogadas_jogador1[num][indexe] = valor
        num += 1

def preenche_jog2(valor):
    global jogadas_jogador2
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
            result =  False
            break
        num += 1
    return result
