# ### Exercício 1: Lista de Números ao Quadrado
# **Objetivo:** Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numbers = list(range(1,11))
for number in numbers:
    print(f"O número {number} ao quadrado é {number**2}")