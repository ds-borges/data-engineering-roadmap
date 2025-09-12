from typing import List

from input_valores import receiving_value


def contar_valores_unicos(lista: List[int]) -> int:
    """
    Função para contar valores únicos em uma lista
    """
    return len(set(lista))


print("Bem vindo a exclusor de duplicatas!!")
print("Avisos o analisador aceita todo tipo de números")

recebendo_numeros: List[float] = receiving_value()
numeros_int: List[int] = [int(num) for num in recebendo_numeros]
# unique_numbers = contar_valores_unicos(recebendo_numeros)

print(f"\nA quantidade de valores únicos são: {contar_valores_unicos(numeros_int)}")
