from typing import List

from input_valores import receiving_value


def calcular_desvio_padrao(valores: List[float]) -> float:
    """
    Função para calcular desvio padrão de uma lista
    """
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia**0.5


print("Bem vindo ao calculador de desvio padrão!!")
print("Avisos o calculador aceita todo tipo de números")

recebendo_numeros: List[float] = receiving_value()

print(
    "\nO desvio padrão da lista fornecida é: "
    f"{(calcular_desvio_padrao(recebendo_numeros)):.2f}"
)
