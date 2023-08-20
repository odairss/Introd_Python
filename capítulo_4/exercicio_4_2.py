#Programa que pergunta a velocidade do carro e exibe uma mensagem se o usuário foi multado ou não.
velocidade = int(input("Informe a velocidade do carro: "))
if velocidade > 80:
    print("Você foi multado!")
    valor = (velocidade - 80) * 5.00
    print("Valor da multa: %5.2f" % valor)
else:
    print("Parabéns! Você não foi multado.")
    
