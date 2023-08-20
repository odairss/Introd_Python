soma = 0
conta_numeros = 0
while True:
    num = int(input("Digite o próximo número inteiro ou 0 para sair: "))
    
    if num == 0:
        break
    
    conta_numeros += 1
    soma += num

print("Quantidade de números digitados: %d" % conta_numeros)
print("Soma dos números digitados: %d" % soma)
print("Média aritmética: %5.2f " % (soma/conta_numeros))
