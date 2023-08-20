# Listagem 6.21 - Simulação de uma fila de banco
ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual: ", fila)
    print("Digite F para adicionar um cliente ao fim da fila,\nou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S): ")
    if operacao == "A":
        if len(fila) > 0:
            atendimento = fila.pop(0)
            print("Cliente %d atendido" % atendimento)
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == "F":
            ultimo += 1 # Incrementa o ticket do novo cliente.
            fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida!\nDigite apenas F, A, ou S!")
            
