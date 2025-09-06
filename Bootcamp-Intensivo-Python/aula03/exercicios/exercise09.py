### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

'''
Instruções de Uso:
    - O programa aceita números inteiros, positivos ou negativos.
    - Você pode separar os números por espaço ou vírgula.

Exemplos de Entrada:
    - Com espaços: "10 5 22 7 8"
    - Com vírgulas: "1, 3, 4, 6"
    - Misto: "10, 20 3 50"

'''

print("Bem vindo ao sistema de validação de números pares, para ajuda leia a docstring")
input_num = input("Digite os números: ")

try:
    # 1. Checa se a entrada está vazia.
    if not input_num:
        raise ValueError("Digite números")
    
    # 2. Se a entrada contém vírgulas, substitui por espaços para unificar o formato.
    if ',' in input_num:
        input_num = input_num.replace(',', " ")
    
    # 3. Divide a string em uma lista de strings de números.
    num_list = input_num.split()

    # 4. Converte cada string da lista para um número inteiro.
    num = [int(n) for n in num_list]

    num_par = []  # Lista para armazenar os números pares.
    
    # 5. Percorre cada número na lista.
    for atual in num:
        # Se o resto da divisão por 2 for 0, o número é par.
        if atual % 2 == 0:
            num_par.append(atual)  # Adiciona o número par à lista.

# Captura erros se o usuário digitar algo que não seja um número.
except ValueError as e:
    print(f"Error: {e}")

# Bloco executado apenas se o "try" for bem-sucedido.
else:
    print(f"Os números pares são: {num_par}")