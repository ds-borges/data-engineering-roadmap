############################################################## Exercício 16 #############################################################

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas. #


# Pegando os valores
print("Avaliando expressões boleanas")
expression_01 = (input("Digite a primeira expressão boleana (true ou false): "))
expression_02 = (input("Digite a segundo expressão boleana (true ou false): "))

# Garantir que as entradas são "true" ou "false"
expression_01 = expression_01.lower() == "true"
expression_02 = expression_02.lower() == "true"

# Comparando as expressões
expression_result = expression_01 and expression_02

print(f" O resultado AND das expressões inseridas é: {expression_result}") 