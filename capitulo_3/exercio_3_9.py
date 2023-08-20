#Programa que recebe a quantidade de dias, horas, minutos e segundos e imprime o total em segundos.
dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))
total_de_segundos = segundos + minutos * 60 + horas * 60 * 60 + dias * 24 * 60 * 60
print("%d dias, %d horas, %d minutos e %d segundos convertidos em segundos é %d segundos. " % (dias, horas, minutos, segundos, total_de_segundos))
