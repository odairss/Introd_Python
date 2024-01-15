string1 = input("Informe a primeira string: ")
string2 = input("Informe a segunda string: ")


n = 0
lista = []

while n < len(string2):
    if string2[n] not in string1:
        lista.append(string2[n])
    n += 1

string3 = ''.join(lista)
print(string3)
