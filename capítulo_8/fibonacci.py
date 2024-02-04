n = int(input("Informe um número: "))

def fibonacci(n):
    fibo = 0
    x = 0
    print(fibo)
    while x <= n:
        if fibo > 1:
            fibo += (fibo - 1)
        else:
            fibo += 1
            print(fibo + (fibo-1))
        print(fibo)
        x += 1

fibonacci(n)
