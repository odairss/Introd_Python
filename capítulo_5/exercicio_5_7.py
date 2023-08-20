num = int(input("Tabuada de ? "))
inicio = int(input("Início: "))
fim = int(input("Fim: "))

while inicio <= fim:
    print("%d + %d = %d " % (num, inicio, (num + inicio)))
    inicio += 1
