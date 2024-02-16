from Compara_String import compara_string

uma_lista = list(range(10))

n = 0
while n < len(uma_lista):
    uma_lista[n] = input("Entre com um frase curta: ")
    n += 1

uma_string = input("Entre com a última frase curta: ")

if compara_string(uma_string, uma_lista):
    print("A última frase está contida entre as primeiras.")
else:
    print("A última frase não está contida entre as primeiras.")
