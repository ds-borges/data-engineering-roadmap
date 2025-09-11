from typing import List


def calcular_media(valores: list[float]) -> float:
    return sum(valores) / len(valores)


lista_numeros: List[float] = []

print("Bem vindo ao analisador de média!!")
print("Avisos o analisador aceita todo tipo de números")
print("-->Para números decimais use ponto<--\n")
try:
    input_user = input("Digite os números desajados: ")

    if "," in input_user:
        input_user = input_user.replace(",", " ")

    lista_numeros = [float(x.strip()) for x in input_user.split()]
except ValueError as e:
    print(f"Error: {e}")
else:
    print(calcular_media(lista_numeros))
