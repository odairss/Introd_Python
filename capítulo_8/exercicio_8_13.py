import random
vezes = 0
while vezes < 3:
    n = random.randint(1,10)
    escolha = int(input("Escolha um número entre 1 e 10: "))
    if n == escolha:
        print("Parabéns, você acertou!")
        break
    else:
        vezes += 1
        if vezes < 3:
            print("Errou. Você ainda tem %d chance(s)." % (3 - vezes))
        else:
            print("Suas chances acabaram.")
