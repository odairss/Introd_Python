#Programa que imprime o resultado de 2 números usando apenas adições.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

contador = 0
resultado = 0

while contador < num2:
    resultado += num1
    contador += 1

print("Resultado: %f" % resultado)
    
