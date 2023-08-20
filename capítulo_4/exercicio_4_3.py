#programa que lê 3 números e imprime o maior e menor

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))


maior = num1
menor = num2

if num2 > num1:
    maior = num2
    menor = num1

if num3 > num1:
    maior = num3
    if num2 > num1:
        menor = num1

if num3 < num2:
    menor = num3

print("Maior: %f" % maior)
print("Menor: %f" % menor)
        
