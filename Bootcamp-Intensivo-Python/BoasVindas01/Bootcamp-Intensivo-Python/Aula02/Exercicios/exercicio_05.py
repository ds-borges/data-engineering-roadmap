#################################### Exercício 05 ####################################

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário. #

# Pegando os valores
print("Vamos elevar o número ao quadrado")
valor_01 = int(input("Digite o número desejado: "))

# Elevando ao quadrado
#valor_total = valor_01 ** 2
valor_total = pow(valor_01, 2)

print(f"O número {valor_01} elevado ao quadrado é: {valor_total}") 