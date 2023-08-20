#Programa que solicita o preço, o percentual de desconto e exibe o valor do desconto e o preço a pagar.
preco = float(input("Informe o preço atual da mercadoria: "))
percentual = float(input("Informe o percentual de desconto: "))

valor_do_desconto = percentual * preco / 100
novo_preco = preco - valor_do_desconto

print("Você recebeu um desconto de: %5.2f reais." % valor_do_desconto)
print("O preço da mercadoria com desconto é %5.2f reais. " % novo_preco )
