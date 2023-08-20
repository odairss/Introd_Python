"""
Programa que solicita o código do produto e a quantidade comprada
para controlar uma máquina registradora
"""


total = 0.0

while True:
    cod = int(input("Código do produto: "))
    if cod == 0:
        break
    quant = int(input("Quantidade: "))
    if cod == 1:
        total = quant  * 0.50
    elif cod == 2:
        total = quant * 1.00
    elif cod == 3:
        total = quant * 4.00
    elif cod == 5:
        total = quant * 7.00
    elif cod == 9:
        total = quant * 8.00
    else:
        print("Código inválido!")

print("Total R$: %5.2f" % total)
    
