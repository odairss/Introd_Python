"""
Função auxiliar para o programa
que percorre duas listas e gera uma terceira
sem elementos repetidos.
"""
def gerador_de_lista(umalista, listagerada):
    a = 0
    while a < len(umalista):
        b = 0
        existe = True
        while b < len(listagerada):
            if str(umalista[a]) == str(listagerada[b]):
                existe = False
            b += 1
        if existe:
            listagerada.append(umalista[a])
        a += 1
        
