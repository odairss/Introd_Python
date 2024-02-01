"""
Exercício 7.10 da pág. 160.

Um jogo da  velha para dois jogadores.

"""

from componentes_do_jogo import *

jogador1 = input("Nome do primeiro jogador: ")
jogador2 = input("Nome do segundo jogador: ")

jogadores = [jogador1,jogador2]

jogadas = 0
jogador = 0

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
                            print(f"Parabéns {jogador}. Você ganhou o jogo!!".upper())
                            resultado = False
                            break
                    elif jogador == jogador2:
                        preenche_tabuleiro(escolha, 2)
                        preenche_jog2(escolha)
                        formata_string()
                        if not confere_se_ganhou(jogadas_jogador2):
                            print(f"Parabéns {jogador}. Você ganhou o jogo!!".upper())
                            resultado = False
                            break
                    informa_posicoes_ocupadas()
                    informa_posicoes_livres()
                    posicao = False
                    jogadas += 1
                else:
                    posicao = True
                    print(f"Essa posição já está ocupada {jogador},\nescolha uma das posições abaixo:")
                    print(posicoes_livres)
    
print()
print("fim!".upper().center(10,':'))
