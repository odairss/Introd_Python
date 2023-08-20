# Listagem 6.53 - Exemplo de dicionário com estoque e operações de venda
# Esse exemplo está na página 132 do livro Introdução à Programação com Python.

estoque = { "tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijao": [100, 1.50]}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]

total = 0

print("Vendas: \n")
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade, preco, custo))
    estoque[produto][0] -= quantidade
    total += custo

print("Custo total: %21.2f\n" % total)
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f \n" % dados[1])
