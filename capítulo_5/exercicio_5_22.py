"""
Programa que exibe um menu com as operações matemáticas
básicas e imprime a tabuada com a operação escolhida
"""
def tabuada ():
    
    escolha = 0

    while escolha != 5:
        print("*"*5+"Escolha a tabuada"+"*"*5)
        print("(1) Adição")
        print("(2) Subtração")
        print("(3) Multiplicação")
        print("(4) Divisão")
        print("(5) Sair")
        escolha = int(input("Sua escolha: "))
        operador = 0
        operando = 0
        if escolha == 1:
            while operando <= 10:
                while operador <= 10:
                    operacao = operando + operador
                    print("%d + %d = %d" % (operando, operador, operacao))
                    operador += 1
                operando += 1
                operador = 0
                print("-"*15)
        elif escolha == 2:
            while operando <= 10:
                while operador <= 10:
                    operacao = operando - operador
                    print("%d - %d = %d" % (operando, operador, operacao))
                    operador += 1
                operando += 1
                operador = 0
                print("-"*15)
        elif escolha == 3:
            while operando <= 10:
                while operador <= 10:
                    operacao = operando * operador
                    print("%d * %d = %d" % (operando, operador, operacao))
                    operador += 1
                operando += 1
                operador = 0
                print("-"*15)
        elif escolha == 4:
            operador = 1
            operando = 1
            while operando <= 10:
                while operador <= 10:
                    operacao = operando / operador
                    print("%d / %d = %d" % (operando, operador, operacao))
                    operador += 1
                operando += 1
                operador = 1
                print("-"*15)
        elif escolha == 5:
            print("Tchau!")
        else:
            print("Opção inválida!")
