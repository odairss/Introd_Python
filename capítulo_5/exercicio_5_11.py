"""
Programa que pergunta o valor do depósito, a taxa de juros mensal,
por quantos meses pretende-se deixar rendendo, exibe os ganhos a cada mês
e os juros totais ao final.
"""

deposito_inicial = float(input("Qual o valor do depósito inicial? "))
taxa_juros = float(input("Qual a taxa de juros informada pelo banco? "))
meses = int(input("Quantos meses você pretende deixar rendendo? "))

total_ganho = deposito_inicial
juros_do_mes = 0.0
total_juros = 0.0
n = 1
print("*******SEUS RENDIMENTOS*******")
print("*"*30)
while n <= meses:
    
    juros_do_mes = total_ganho * taxa_juros
    total_ganho += juros_do_mes
    total_juros += juros_do_mes
    
    print("%dº mês:" % n)
    print("Juros: %5.2f" % juros_do_mes)
    print("Acumulado: %5.2f" % (total_ganho))
    n += 1
    print("*"*30)

print("Total de juros ganhos: %5.2f" % total_juros)
    
