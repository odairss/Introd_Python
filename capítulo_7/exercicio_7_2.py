string1 = input("Informe o valor da primeira string: ")
string2 = input("Informe o valor da segunda string: ")

lista_de_indices = []

num = 0

while num < len(string2):
    if string1.find(string2[num]) > -1:
                    lista_de_indices.append(string2[num])
    num += 1

string3 = ''.join(lista_de_indices)
print(string3)
