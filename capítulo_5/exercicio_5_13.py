"""
Programa que pergunta o valor da dívida, a taxa de juros, o valor da parcela mensal de pagamento
e imprime em quantos meses a dívida será paga e o total de juros pago.
"""

valor_inicial_da_divida = float(input("Qual o valor inicial da sua dívida? "))
taxa_juros = float(input("Qual a taxa de juros mensais? "))
pagamento_mensal = float(input("Quanto deseja pagar por mês? "))

total_de_meses = 0
divida_atual = valor_inicial_da_divida
valor_dos_juros = 0.0
juros_total = 0.0
total_pago = 0.0
conta_meses = 0
print("Valor contratado R$: %5.2f" % valor_inicial_da_divida)
print("Taxa de juros: %2.3f" % taxa_juros)
while divida_atual > 0:
    conta_meses += 1
    print("*" * 20)
    print("%d mês:" % conta_meses)
    
    valor_dos_juros = divida_atual * taxa_juros
    print("Juros do mês R$:%5.2f" % valor_dos_juros)
    divida_atual += valor_dos_juros
    print("Dívida atual R$:%5.2f" % divida_atual)
    juros_total += valor_dos_juros
    
    if divida_atual >= pagamento_mensal:
        print("Valor pago R$:%5.2f" %pagamento_mensal)
        divida_atual -= pagamento_mensal
        total_pago += pagamento_mensal
    else:
        print("Valor pago R$:%5.2f" % divida_atual)
        total_pago += divida_atual
        divida_atual -= divida_atual
    
    print("Total pago R$:%5.2f" % total_pago)
    total_de_meses += 1

print("*" * 20)
print("A dívida será paga em %d mese(s)." % total_de_meses)
print("Valor total pago: %5.2f" % total_pago)
print("Total de juros pagos: %5.2f" % juros_total)
