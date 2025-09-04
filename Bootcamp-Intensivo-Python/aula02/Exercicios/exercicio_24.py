########## Exercício 24 #########

# 24: Classificador de Números. #

import math

print("Bem-vindo(a) à verificação de números.")
print("Aqui verificaremos se é positivo ou negativo, par ou impar, é primo ou não e se é perfeito ou não.\n")

try:
    # Pegando um número
    num = int(input("Por favor, digite um númmero para verificar: "))

    # Verifica se é positivo
    if num==0:
        p_n = "não é positivo nem negativo"
    elif num > 1:
        p_n = "é positivo"
    else:
        p_n = "é negativo" 
    
    # Verifica se é par
    if num % 2 == 0:
        p_i = "é par"
    else:
        p_i = "é impar"

    # Verifica se é primo
    primo = "não é primo"
    if num > 1:
        primo = "é primo"
        for cont in range(2, int(math.sqrt(num)) + 1):
            if num % cont == 0:
                primo = "não é primo"
                break
    
    #Verificar se é perfeito
    perfeito = "não é perfeito"
    if num > 1:
        verifica_perfeito = 1
        for cont in range(2, num-1, + 1):
            if num % cont == 0:
                verifica_perfeito += cont
        if (num == verifica_perfeito):
            perfeito = "é perfeito"
        
    print(f"O número: {num} {p_n}, {p_i}, {primo} e {perfeito}")
# Captura qualquer erro
except ValueError as e:
    print(f"Erro: Por favor, digite apenas números. Detalhes: {e}")