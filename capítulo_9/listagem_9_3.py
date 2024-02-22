"""
Listagem 9.3 - Impressão dos parâmetros passados na linha de comando

"""
import sys
print("Número de parâmetros: %d" % len(sys.argv))
for n, p in enumerate(sys.argv):
    print("Parâmetro %d = %s" % (n,p))
