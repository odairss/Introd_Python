"""
Listagem 8.14 - Função recursiva de Fibonacci (pág. 172).

Este programa utiliza uma função para calcular o enésimo termo da sequência de Fibonacci.

"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
