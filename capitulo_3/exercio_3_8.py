#Programa que recebe um número em metros e exibe em centímetros.

valor_em_metros = float(input("Informe o valor em metros: "))
valor_em_centimetros = int(valor_em_metros * 100)
print("%4.2f metros é igual a %d centímetros. " % (valor_em_metros, valor_em_centimetros))
