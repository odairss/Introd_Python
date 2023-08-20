"""
Programa que pergunta o valor do depósito, a taxa de juros mensal, o aporte mensal,
por quantos meses pretende-se deixar rendendo, exibe os ganhos a cada mês
e os juros totais ao final.
"""

deposito_inicial = float(input("Qual o valor do depósito inicial? "))
taxa_juros = float(input("Qual a taxa de juros informada pelo banco? "))
meses = int(input("Quantos meses você pretende deixar rendendo? "))
aporte_mensal = float(input("Qual será o valor do aporte mensal? "))

acumulado = deposito_inicial
juros_do_mes = 0.0
total_juros = 0.0
n = 1
print("*******SEUS RENDIMENTOS*******")
print("*"*30)
print("Investimento inicial: %5.2f" % deposito_inicial)
while n <= meses:
    
    acumulado += aporte_mensal
    juros_do_mes = acumulado * taxa_juros
    acumulado += juros_do_mes
    total_juros += juros_do_mes
    
    print("%dº mês:" % n)
    print("Aporte mensal: %5.2f" % aporte_mensal)
    print("Juros: %5.2f" % juros_do_mes)
    print("Acumulado: %5.2f" % (acumulado))
    n += 1
    print("*"*30)

print("Total de juros ganhos: %5.2f" % total_juros)
    
