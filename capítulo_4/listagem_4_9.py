valor_da_casa = float(input("Valor da casa? "))
salario = float(input("Quanto você ganha por mês? "))
num_parcelas = int(input("Em quantas parcelas você quer dividir? "))


limite = salario * 0.30

valor_da_parcela = valor_da_casa / num_parcelas

if valor_da_parcela < limite:
    print("30 do seu salário equivale a R$: %4.2f" % limite)
    print("Valor das parcelas R$: %4.2f" % valor_da_parcela)
    print("Empréstimo aprovado! ")
else:
    print("30 do seu salário equivale a R$: %4.2f" % limite)
    print("Valor das parcelas R$: %4.2f" % valor_da_parcela)
    print("EMPRÉSTIMO NÃO APROVADO!")
