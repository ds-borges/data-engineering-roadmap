################################################### Exercício 18 ###################################################

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor. #

# Pegando os valores
print("Invertendo as expressões boleanas")
expression = (input("Digite a expressão boleana (true ou false): "))

# Garantir que as entradas são "true" ou "false" e já inverter elas
expression = not (expression.lower() == "true")

print(f"O resultado da inversão da expressão boleana é: {expression}") 