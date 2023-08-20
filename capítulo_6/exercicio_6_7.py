"""
Programa que lê uma expressão com parênteses e verifica se os
parênteses foram abertos e fechados na ordem correta.
"""
parenteses = input("Digite sua expressão utilizando somente parenteses: ")
a = 0
count_parenteses = 0

pilha = []
while a < len(parenteses):
    if parenteses[a] == "(":
        count_parenteses += 1
        pilha.append(count_parenteses)
        print(pilha)
    elif parenteses[a] == ")":
        if len(pilha) > 0:
            count_parenteses -= 1
            pilha.pop(-1)
            print(pilha)
        else:
            print("Pilha vazia! Nada para retirar.")

    a += 1


if count_parenteses != 0:
    print("Ficou %d parenteses aberto(s)" % count_parenteses)
else:
    print("Todos os parênteses foram abertos e fechados na ordem correta")
