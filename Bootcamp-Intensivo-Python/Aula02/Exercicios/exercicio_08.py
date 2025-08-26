############################################### Exercício 08 ###############################################

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário). #

# Pegando os valores
print("Vamos calcular a potência de um número")
valor_01 = int(input("Digite a base desejada: "))
valor_02 = int(input("Digite o expoente desejado: "))

# Realizando a potência do número A base sempre significa o valor que vão O número vai ser repetido
#valor_total = valor_01 ** valor_02
valor_total = pow(valor_01, valor_02)

print(f"O número {valor_01} elevado a {valor_02} é: {valor_total}") 