#Programa que solicita o valor do salário, uma porcentagem e calcula o aumento de salário com base nessa porcentagem.
salario = float(input("Informe o valor do salário: "))
porcentagem = float(input("Informe a porcentagem do aumento: "))
aumento = porcentagem * salario / 100
novo_salario = aumento + salario

print("Você recebeu um aumento de R$: %5.2f reais." % aumento)
print("Seu novo salário é de R$: %5.2f reais." % novo_salario)
