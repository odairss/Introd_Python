"""

Programa com duas formas de calcular a sequência de Fibonacci.

"""

# ===PRIMEIRA VERSÃO ===

valor = input("Informe um número para ver a sequência de Fibonacci: ")
if valor.isdigit():
    valor = int(valor)
    fibo = [0,1]
    n=1
    while n < valor:
        fibo.append(fibo[n-1]+fibo[n])
        n += 1
    str_fibo = ''
    for n in fibo:
        str_fibo += str(n) + ', '
    print(str_fibo.rstrip(', '))
else:
    print("Precisa ser um número.")

# === SEGUNDA VERSÃO ===

valor = int(input("Informe um número para ver a sequência de Fibonacci: "))
início = 0
antecessor = 1
ante_antecessor = 1

n = 0
str_fibo = str(início) + ', '+ str(ante_antecessor) + ', ' + str(antecessor) + ', '
while n < (valor-2):
    sucessor = ante_antecessor + antecessor
    ante_antecessor = antecessor
    antecessor = sucessor
    str_fibo += str(sucessor) + ', '
    n += 1
print(str_fibo.rstrip(', '))

# ===SOLUÇÃO DO CHAT GPT===
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

# Teste
n = int(input("Digite o número de termos da sequência Fibonacci desejados: "))
fibonacci_sequence = fibonacci(n)
print("A sequência de Fibonacci com", n, "termos é:", fibonacci_sequence)
