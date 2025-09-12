from typing import List

from input_valores import receiving_value


def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    """
    Função para converter celsius para fahrenheit em uma lista
    """
    return [(9 / 5) * temp + 32 for temp in temperaturas_celsius]


print("Bem vindo ao conversor de temperatura!!")
print("Avisos o conversor aceita todo tipo de números")

recebendo_numeros: List[float] = receiving_value()

print(
    f"\nAs temperaturas em fahrenheit são: {celsius_para_fahrenheit(recebendo_numeros)}"
)
