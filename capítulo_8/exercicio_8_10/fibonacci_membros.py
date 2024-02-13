def fibonacci(valor):
    fibo = [0,1]
    n = 1
    while n < valor:
        fibo.append(fibo[n-1]+fibo[n])
        n += 1
    return fibo


def imprime_fibonacci(fibonacci_array):
    str_fibo = ''
    for n in fibonacci_array:
        str_fibo += str(n) + ', '
    return str_fibo.rstrip(', ')
