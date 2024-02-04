INDEXES = [[1,2,3], [4,5,6], [7,8,9]]
TABULEIRO = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

COMBINACOES_VENCEDORAS = [[3,6,9],[2,5,8],[1,4,7],[4,5,6],[1,2,3],[1,5,9],[7,8,9],[3,5,7]]

JOGADAS_JOGADOR1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

JOGADAS_JOGADOR2 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

POSICOESESCOLHIDAS = list()


POSICOES_LIVRES = list(range(1,10))

def preenche_tabuleiro(esclh, jog):
    global TABULEIRO
    if jog == 1:
        if esclh <= 3:
            TABULEIRO[0][INDEXES[0].index(esclh)] = 'x'
        elif esclh <= 6:
            TABULEIRO[1][INDEXES[1].index(esclh)] = 'x'
        else:
            TABULEIRO[2][INDEXES[2].index(esclh)] = 'x'
    elif jog == 2:
        if esclh <= 3:
            TABULEIRO[0][INDEXES[0].index(esclh)] = 'o'
        elif esclh <= 6:
            TABULEIRO[1][INDEXES[1].index(esclh)] = 'o'
        else:
            TABULEIRO[2][INDEXES[2].index(esclh)] = 'o'     

def formata_string():
    string_jogo = ''  
    for line in TABULEIRO:
        for ln in line:
            string_jogo += str(ln) + '|'
        string_jogo = string_jogo.rstrip('|')
        string_jogo += '\n-+-+-\n'
    string_jogo = string_jogo[0:29].upper()
    print(string_jogo)

def informa_posicoes_livres():
    livres = ''
    for position in POSICOES_LIVRES:
        livres += ', ' + str(position)
    print(f"Posições livres até o momento: {livres}")
    print(":".rjust(50,':'))

def informa_posicoes_ocupadas():
    escolhidas = ''
    for pos in POSICOESESCOLHIDAS:
        escolhidas += ', ' + str(pos)
    print(f"Posições escolhidas até o momento: {escolhidas}")
    
def preenche_jog1(valor):
    global JOGADAS_JOGADOR1
    num = 0
    while num < 8:
        if valor in COMBINACOES_VENCEDORAS[num]:
            indexe = COMBINACOES_VENCEDORAS[num].index(valor)
            JOGADAS_JOGADOR1[num][indexe] = valor
        num += 1

def preenche_jog2(valor):
    global JOGADAS_JOGADOR2
    num = 0
    while num < 8:
        if valor in COMBINACOES_VENCEDORAS[num]:
            indexe = COMBINACOES_VENCEDORAS[num].index(valor)
            JOGADAS_JOGADOR2[num][indexe] = valor
        num += 1

def confere_se_ganhou(jogadas):
    num = 0
    result = True
    while num < 8:
        if jogadas[num] == COMBINACOES_VENCEDORAS[num]:
            result =  False
            break
        num += 1
    return result
