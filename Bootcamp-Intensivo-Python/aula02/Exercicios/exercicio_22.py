########## Exercício 22 #########

# 22: Verificador de Palíndromo #

# Pegando os valores
print("Verificador de palíndromo")
while True:
    try: 
        # Recebe uma palavra
        expression = (input("Digite uma palavra: "))
        
        # Verifica se a entrada não é uma string vazia e se contém apenas letras
        if not expression or not expression.isalpha():
            raise ValueError("Entrada inválida! Por favor, digite apenas letras.")
        
        # Inverte a string
        palindromo = expression[::-1]

        # Se a palavra for palíndromo será encerrado
        if palindromo == expression :
            print("Esta palavra é um palindromo !")
            break
    
         # Se a palavra não for um palíndromo, gerará um erro
        else:
            raise ValueError("Esta palavra não é um palíndromo !!!")
    
    # Captura qualquer erro
    except Exception as e:
        print(f"Ocorreu um erro: {e}\n")
