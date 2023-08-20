# Listagem 6.35 - Cotrole da utilização de salas de um cinema

lugares_vagos = [10,2,1,3,0]

while True:
    sala = int(input("Sala (0 sair): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala-1] == 0:
        print("Desculpe, sala lotada! ")
    else:
        lugares = int(input("Quantos lugares você deseja (%d vagos): " % lugares_vagos[sala-1]))
    if lugares > lugares_vagos[sala-1]:
        print("Esse número de lugares não está disponível. ")
    elif lugares < 0:
        print("Número inválido")
    else:
        lugares_vagos[sala-1] -= lugares
        print("%d lugares vendidos" % lugares)
print("Utilização das salas")
for x, l in enumerate(lugares_vagos):
    print("Sala %d - %d lugar(es) vazio(s)" % (x+1, 1))
