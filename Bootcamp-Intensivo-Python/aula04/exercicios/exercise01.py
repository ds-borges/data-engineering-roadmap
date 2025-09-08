"""
Exercício 1: Lista de Números ao Quadrado

Objetivo:
    Elevar ao quadrado cada número de 1 a 10 e imprimir o resultado.

Instruções:
    - O programa cria uma lista de números inteiros de 1 a 10.
    - Ele percorre a lista e, para cada número, calcula o seu quadrado.
    
Saída Esperada:
    O programa imprimirá uma lista de 10 linhas,
    mostrando o número original e o seu valor ao quadrado.
"""

# Cria uma lista de números inteiros de 1 a 10 usando a função `range()`.
numbers: list = list(range(1, 11))

# Percorre a lista `numbers` usando um loop `for`.
for number in numbers:
    # Calcula o quadrado do número atual e imprime a mensagem formatada.
    print(f"O número {number} ao quadrado é {number**2}")