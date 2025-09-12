from typing import List

from input_valores import receiving_value


def calcular_media(valores: list[float]) -> float:
    """
    Função simples que calcula uma média de valores
    """
    return sum(valores) / len(valores)


lista_numeros: List[float] = []

print("Bem vindo ao analisador de média!!")
print("Avisos o analisador aceita todo tipo de números")
print("-->Para números decimais use ponto<--\n")

recebendo_numeros: List[float] = receiving_value()
lista_numeros = calcular_media(recebendo_numeros)
print(lista_numeros)
