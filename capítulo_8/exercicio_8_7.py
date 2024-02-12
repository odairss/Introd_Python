"""
Exercício 8.7 dá pág. 172:

Este programa calcula o máximo divisor comum (MDC) entre dois números a e b, onde a > b.

"""

print("\nSOLUÇÃO INICIALMENTE ARRANJADA POR MIM:\n")

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B, onde B < A: "))

num = 1
divisor = 1
n = 1

def mdc(n):
    global divisor
    if n <= b:
        if a%n==0 and b%n==0:
            divisor = n
        mdc(n+1)
    return divisor

print(f"O máximo divisor comum entre {a} e {b} é: {mdc(num)}")


print("\n\nSOLUÇÃO ARRANJADA APÓS CONSULTAR O CHAT GPT:\n")

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B, onde B < A: "))
resto = 0
def mdc_gpt():
    global b
    global a
    global resto
    resto = a%b
    if resto > 0:
        a = b
        b = resto
        mdc_gpt()
    return b
        

print(f"O máximo divisor comum entre {a} e {b} é: {mdc_gpt()}")
