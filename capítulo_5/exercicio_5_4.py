fim = int(input("Digite o último número ímpar a imprimir: "))

x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1
