"""
Programa que percorre duas listas e gera uma terceira
sem elementos repetidos.
"""
import exercicio_6_3_funcao
        
listaA = ["odair", 1, 2.3, True, 3, "odair"]
listaB = [10, 20, True, False, "Damiana", 45.2, "odair", 10, "Damiana", "Damiana", "Damiana"]
listaC = []

exercicio_6_3_funcao.gerador_de_lista(listaA, listaC)
exercicio_6_3_funcao.gerador_de_lista(listaB, listaC)
print(listaC)
