from typing import List

from input_valores import receiving_value


def filtrar_acima_de(valores: list[float], limite) -> float:
    """
    Função simples que filtra os números acima de
    um valor definido pelo usuário
    """

    resultado = []

    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado


print("Bem vindo ao analisador de valores acima do limite!!")
print("Avisos o analisador aceita todo tipo de números")

recebendo_numeros: List[float] = receiving_value()
limite_user = int(input("Digite um valor para limite: "))

print(
    f"\nOs valores acima do limite {limite_user}, "
    + f"são {filtrar_acima_de(recebendo_numeros,limite_user)}"
)
