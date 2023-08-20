#Programa que calcula o preço da conta de energia elétrica

consumo = float(input("Seu consumo em kWh? "))
tipo = str(input("Tipo de instalação? ")) # R = Residencial, C = Comercial, I = Industrial.
preco = 0.0

if tipo == "R":
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif tipo == "C":
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif tipo == "I":
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60

print("Preço R$:%4.2f" %preco)
