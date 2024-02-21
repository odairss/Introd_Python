"""
Listagem 9.2 - Abrindo, lendo e fechando um arquivo
pág. 190

"""

arquivo = open("números.txt", 'r')

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
