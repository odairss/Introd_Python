string1 = input("Informe a primeira string: ")
string2 = input("Informe a segunda string: ")


n = 0
lista = []

while n < len(string2):
    if string2[n] not in string1 and string2[n] != ' ':
        if string2[n] not in lista:
            lista.append(string2[n])
    n += 1

n = 0

while n < len(string1):
    if string1[n] not in string2  and string1[n] != ' ':
        if string1[n] not in lista:
            lista.append(string1[n])
    n += 1

string3 = ''.join(lista)
print(string3)
