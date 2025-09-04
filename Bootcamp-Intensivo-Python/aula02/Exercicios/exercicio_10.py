####################################### Exercício 10 #######################################

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada. #

import math

# Pegando o valor do raio
print("Vamos calcular a área de um círculo")
raio = int(input("Digite o valor do raio: "))

# Calculando a área do círculo e arredondando o resultado para ter 2 casas decimais
area = round(math.pi * pow(raio, 2), 2)

print(f" O circulo de raio {raio} tem a área de {area}") 