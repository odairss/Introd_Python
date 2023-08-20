#Programa que pergunta a distância e calcula o preço da passagem.

distancia = float(input("Informe a distância da sua viagem em quilômetros: "))

preco = 0

if distancia <= 200:
    preco  = distancia * 0.50
else:
    preco = distancia * 0.45


print("Sua viagem custará: %5.2f" % preco)
