#Programa que pergunta o salário e calcula o aumento.

salario = float(input("Qual o valor do seu salário? "))

aumento = salario * 0.15

if salario > 1250.00:
	aumento = salario * 0.10
	
print("Valor do seu aumento: R$%10.2f" % aumento)
print("Seu novo salário: R$%10.2f " % (salario + aumento))

