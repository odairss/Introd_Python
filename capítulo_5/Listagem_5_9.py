# Tabuada de adição de 1 a 10 de um número informado pelo usuário.

num = int(input("Tabuada de ? "))

x = 1

while x <= 10:
    print("%d + %d = %d " % (num, x, (num + x)))
    x += 1
