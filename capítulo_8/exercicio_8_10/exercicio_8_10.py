from fibonacci_membros import fibonacci, imprime_fibonacci

while True:
    valor = input("Informe um número para ver a sequência e Fibonacci: ")
    if valor.isdigit():
        fibonacci_list = fibonacci(int(valor))
        print(imprime_fibonacci(fibonacci_list))
        break
    else:
        print("Precisa ser um número inteiro.")
    
