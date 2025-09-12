from typing import List

from input_valores import receiving_value


def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """
    Função para encontrar valores ausentes em uma sequência
    """
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))


print("Bem vindo a localizador de números ausentes!!")
print("Avisos o analisador aceita todo tipo de números")

recebendo_numeros: List[float] = receiving_value()
numeros_int: List[int] = [int(num) for num in recebendo_numeros]

print(
    f"\nOs valores: {encontrar_valores_ausentes(numeros_int)} "
    f"foram identificados como ausentes na lista: {numeros_int}"
)
