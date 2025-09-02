################################ Exercício 09 ################################

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit. #

# Pegando a temperatura
print("Digite a temperatura em Celsius para transformar em Fahrenheit")
celsius = float(input(" Digite a temperatura em Celsius: "))

# Convertendo para Fahrenheit e arredondando para ter apenas 2 casas decimais
Fahrenheit = round((celsius * 1.8) +32, 2)
print(f"A temperatura {celsius} em Celsius é igual {Fahrenheit} em Fahrenheit") 