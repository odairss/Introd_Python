#Programa que calcula o preço do aluguel de um carro a um custo fixo de 60 reais por dia e 0,15 centavos por km rodados.
km_rodados = float(input("Você rodou quantos quilômetros? "))
quant_dias = int(input("Por quantos dias você alugou o carro? "))

custo_por_dia = quant_dias * 60.00
custo_por_km = km_rodados * 0.15

print("O valor a pagar é: %5.2f" % (custo_por_dia + custo_por_km))
