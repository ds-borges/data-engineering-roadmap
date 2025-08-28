# Define a string com a expressão
expression = (input("Qual conta iremos fazer?\n "))

# Usa a função eval() para calcular o valor da expressão
try:
    resultado = eval(expression)
    print(f"O resultado da conta é: {resultado}")
except Exception as e:
    print(f"Ocorreu um erro ao tentar avaliar a expressão: {e}")