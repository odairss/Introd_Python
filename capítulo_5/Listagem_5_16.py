# Listagem 5.16 - Impressão de tabuadas sem repetições aninhadas

tabuada = 1
numero = 1

while tabuada <= 10:
    print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
    numero += 1
    if numero == 11:
        numero = 1
        tabuada +=1
