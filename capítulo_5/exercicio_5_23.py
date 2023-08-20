"""
Programa que lê um número e verifica se é número primo.
"""
num = 1
while num != 0:
    num = int(input("Informe um número: "))
    resultado = True

    if num > 2:
        if num % 2 == 0:
            resultado = False

    if num == 0 or num == 1:
        resultado = False

    n = 2
    while n < num:

        if num % n == 0:
            resultado = False
            break
        else:
            n += 1

    if resultado:
        print("%d é número primo" % num)
    else:
        print("%d não é número primo" % num)
