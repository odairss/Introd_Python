#Programa que calcula a redução do tempo de vida de um fumante.

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Quantos anos faz que você fuma? "))

cigarros_fumados = anos * 365 * cigarros_por_dia

#print("Em %d anos você já fumou %d cigarros." % (anos, cigarros_fumados))

#minutos_fumando = anos * 365 * 24 * 60

minutos_de_vida_reduzidos = cigarros_fumados * 10



#print("Você já fumou por %d minutos. " % minutos_fumando)

#print("Você já reduziu seu tempo de vida em %d minutos." % minutos_de_vida_reduzidos)
print("Você já reduziu seu tempo de vida em %d dias. " % int(minutos_de_vida_reduzidos / 60 / 24))
#print("Que equivalem a %4.2f anos da sua vida. " % (float(minutos_de_vida_reduzidos / 60 / 24)/365))
