###### Exercício 23 ######

# 23: Calculadora Simples #

print("Bem-vindo(a) à sua Calculadora Simples.")
print("Por favor, siga as instruções para realizar a sua conta.")

try:    
    # Pegando os valores
    num_01 = float(input("Digite o primeiro número: "))
    operation = input("Escolha uma operação matemática(* / + -): ")
    num_02 = float(input("Digite o segundo número: "))

    if operation == "*":
        print(f"O resultado dessa operação é {num_01 * num_02}")
    elif operation == "/":
        if num_02 != 0:
            print(f"O resultado dessa operação é {num_01 / num_02}")
        else:
            raise ValueError("Divisão por zero não permitdida.")
    elif operation == "+":
        print(f"O resultado dessa operação é {num_01 + num_02}")
    elif operation == "-":
        print(f"O resultado dessa operação é {num_01 - num_02}")
    # Se o simbolo de entrada for incorreto
    else: 
        raise ValueError("Operação matemátixa inválida! Encerrando.")

# Captura qualquer erro
except ValueError as e:
    print(f"Erro: Por favor, digite apenas números. Detalhes: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")