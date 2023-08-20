"""
Programa que lê um número e verifica se é número primo.
"""
def num_primos():
    num = int(input("Informe um número: "))


    primos = ""

    if num >= 2:
        n = 2
        while n <= num:
            if n % 2 != 0:
                iterador = 1
                contador = 0
                while iterador <= n:
                    if n % iterador == 0:
                        contador += 1
                    iterador += 1
                if contador == 2:
                    primos += "-" + str(n)
            elif n == 2:
                primos += str(n)

            n += 1

    print("Números primos até %d:\n%s" % (num, primos))

num_primos()
