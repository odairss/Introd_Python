while True:
    valor = float(input("Digite o valor a pagar: "))
    
    if valor == 0:
        break
    
    while valor > 0:
        if valor >= 100.00:
            notas_100 = int(valor / 100.00)
            print("Notas de 100,00: %d" % notas_100)
            valor -= notas_100 * 100.00
        elif valor >= 50.00:
            notas_50 = int(valor / 50.00)
            print("Notas de 50,00: %d" % notas_50)
            valor -= notas_50 * 50.00
        elif valor >= 20.00:
            notas_20 = int(valor / 20.00)
            print("Notas de 20,00: %d" % notas_20)
            valor -= notas_20 * 20.00
        elif valor >= 10.00:
            notas_10 = int(valor / 10.00)
            print("Notas de 10,00: %d" % notas_10)
            valor -= notas_10 * 10.00
        elif valor >= 5.00:
            notas_5 = int(valor / 5.00)
            print("Notas de 5,00: %d" % notas_5)
            valor -= notas_5 * 5.00
        elif valor >= 2.00:
            notas_2 = int(valor / 2.00)
            print("Notas de 2,00: %d" % notas_2)
            valor -= notas_2 * 2.00
        elif valor >= 1.00:
            moedas_1 = int(valor / 1.00)
            print("Moedas de 1,00: %d" % moedas_1)
            valor -= moedas_1 * 1.00
        elif valor >= 0.50:
            moedas0_50 = int(valor / 0.50)
            print("Moedas de 0,50: %d" % moedas0_50)
            valor -= moedas0_50 * 0.50
        elif valor >= 0.25:
            moedas0_25 = int(valor / 0.25)
            print("Moedas de 0,25: %d " % moedas0_25)
            valor -= moedas0_25 * 0.25
        elif valor >= 0.10:
            moedas0_10 = int(valor / 0.10)
            print("Moedas de 0,10: %d " % moedas0_10)
            valor -= moedas0_10 * 0.10
            valor = int(valor)
        elif valor >= 0.05:
            moedas0_05 = int(valor / 0.05)
            print("Moedas de 0,05: %d " % moedas0_05 )
            valor -= moedas0_05 * 0.05
            valor = int(valor)

        print(valor)
            
    print("*"*40)


