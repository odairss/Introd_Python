"""
Programa que ler 2 números,
pergunta a operação que deve ser
realizada e exibe o resultado.
"""

num1 = float(input("Qual o primeiro número? "))
num2 = float(input("Qual o segundo número? "))

operacao = -1

while 1 > operacao or operacao > 5:
    print("Que tipo de operação você deseja realizar?")
    print(" "*10 + "(1) Adição")
    print(" "*10 + "(2) Subtração")
    print(" "*10 + "(3) Multiplicação")
    print(" "*10 + "(4) Divisão")
    operacao = int(input("Escolha um dos números acima correspondente a operação escolhida: "))
    if operacao == 1:
        print("Você escolheu opção (1) Adição:")
        print("%f + %f = %f" % (num1, num2, (num1 + num2)))
    elif operacao == 2:
        print("Você escolheu opção (2) Subtração:")
        print("%f - %f = %f" % (num1, num2, (num1 - num2)))
    elif operacao == 3:
        print("Você escolheu opção (3) Multiplicação:")
        print("%f * %f = %f" % (num1, num2, (num1 * num2)))
    elif operacao == 4:
        print("Você escolheu opção (4) Divisão:")
        print("%f / %f = %f" % (num1, num2, (num1 / num2)))
    else:
            print("Opção inválida. Para realizar uma das operações, escolha um número entre 1 e 4")
            print("*"*80)
