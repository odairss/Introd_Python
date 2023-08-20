"""
Programa que altera a Listagem 6.21 de forma a poder trabalhar com vários
comandos digitados de uma só vez.
"""
# Listagem 6.21 - Simulação de uma fila de banco
ultimo = 10
fila = list(range(1,ultimo+1))
sair = ""
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual: ", fila)
    print("Digite F para adicionar um cliente ao fim da fila,\nou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S): ")
    operacao = list(operacao)
    a = 0
    while a < len(operacao):
        if operacao[a] == "A":
            if len(fila) > 0:
                atendimento = fila.pop(0)
                print("Cliente %d atendido" % atendimento)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[a] == "F":
                ultimo += 1 # Incrementa o ticket do novo cliente.
                fila.append(ultimo)
                print("Fila atual: ", fila)
        elif operacao[a] == "S":
            sair = "S"
            print("Saindo...")
            break
        else:
            print("Operação inválida!\nDigite apenas F, A, ou S!")
        a += 1

    if sair == "S":
        break
