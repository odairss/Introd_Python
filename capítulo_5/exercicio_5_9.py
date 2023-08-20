"""
Programa que ler dois números, imprime o resultado
e o resto da divisão do primeiro pelo segundo usando somente
a operação de adição e subtração.
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

dividendo = num1
divisor = num2
resultado = 0

while num1 >= num2:
    num1 -= num2
    resultado += 1

print("%f / %f = %d" % (dividendo, divisor, resultado))

resto = num1

print("Resto: %f " % resto)
