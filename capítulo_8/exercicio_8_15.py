import types

uma_lista = [1,["um elemento",{'a':5,'b':'Odair'},4.6,10],5.5, 14,15,[[4,6,6],["odair","soares",'de','souza',[0.3,8.45]]]]

nivel = 0

def imprime_elementos(elemento, n):
    n += 1
    if type(elemento) == str:
        print("."*n + elemento)
    elif type(elemento) == int:
        print("."*n + str(elemento))
    elif type(elemento) == float:
        print("."*n + str(elemento))
    elif type(elemento) == list:
        for e in elemento:
            imprime_elementos(e, n)
    elif type(elemento) == dict:
        for key in elemento:
            imprime_elementos(key, n)


imprime_elementos(uma_lista, nivel)
