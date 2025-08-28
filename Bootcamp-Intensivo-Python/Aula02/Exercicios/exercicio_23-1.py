###### Exercício 23 ######

# 23: Calculadora Simples #

print("Bem-vindo(a) à sua Calculadora Simples.")


# Define a string com a expressão
expression = (input("Por favor, digite a conta completa. Exp (2+2): "))

# Usa a função eval() para calcular o valor da expressão
try:
    if "+" in expression or "-" in expression or "*" in expression or "/" in expression:
        print(f"O resultado da conta é: {eval(expression)}")
    else:
        raise ValueError("Operação matemática inválida! Encerrando.")

# Captura qualquer erro
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")