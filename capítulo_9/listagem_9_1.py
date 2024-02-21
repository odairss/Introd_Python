"""
Listagem 9.1 - Abrindo, escrevendo e fechando um arquivo
pág. 189

"""

arquivo = open("números.txt", 'w')

texto = ''

for linha in range(1,1001):
    texto += str(linha) + ', '


texto = texto.rstrip(', ')
texto += '.'

arquivo.write(texto)

arquivo.close()
