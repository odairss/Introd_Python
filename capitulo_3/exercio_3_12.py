#Programa que solicita a distância e a velocidade, calcula e exibe o tempo de uma viagem.
distancia = float(input("Informe a distância a percorrer em Km: "))
velocidade = float(input("Informe a que velocidade média você pretende dirigir em Km/h: "))

duracao_da_viagem = distancia / velocidade

print("Sua viagem durará %4.2f horas. " % duracao_da_viagem)

espacador = "*" * 50

print(espacador)
duracao_real_da_viagem = float(input("Informe a duração real em horas da sua viagem: "))
distância_real_percorrida = float(input("Informe a distância real percorrida em quilômetros: "))

print("Você percorreu %5.0f km em %4.2f horas a uma velocidade de %.2f km/h" % (distância_real_percorrida, duracao_real_da_viagem, distância_real_percorrida / duracao_real_da_viagem))
