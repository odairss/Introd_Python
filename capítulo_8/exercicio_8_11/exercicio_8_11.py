from valida_string import valida_string


minimo = 20
maximo = 30

while True:
    s = input("Entre com uma frase curta contendo entre 20 e 30 caracteres: ")
    if valida_string(s, minimo, maximo):
        print("Você digitou: " + s)
        print(f"Parabéns! Essa frase é composta por {len(s)} caracteres e atende aos requisitos.")
        break
    else:
        print("String inválida!")
