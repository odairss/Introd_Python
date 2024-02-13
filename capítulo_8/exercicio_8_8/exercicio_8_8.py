"""
Exercício 8.8 da pág. 172

calcula o Mínimo Múltiplo Comum (MMC).
Obs.: Não utilizei a solução indicada pelo livro.
Não entendi a expressão matemática ilustrada no exercício.

"""
from elementos import calc_primos, calc_mmc
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")

num_a = int(input("Informe um número A: "))
num_b = int(input("Informe um número B: "))


str_result = "O Mínimo Múltiplo Comum (MMC) de " + "{:n}".format(num_a) + " e " + "{:n}".format(num_b) + " é: "


primos = calc_primos(num_a, num_b)
mmc = calc_mmc(primos)

print(str_result + "{:n}".format(mmc))










