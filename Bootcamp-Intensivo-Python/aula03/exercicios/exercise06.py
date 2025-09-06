### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

import string # Importa o módulo 'string' para lidar com pontuação.

from collections import Counter

try:
    # 1. Solicita a entrada do usuário
    log = input("Dê os detalhes da transação: ")
    if not log:
        raise ValueError("A entrada não pode ser vazia !!")
except ValueError as e: 
    print(f"Error: {e}")
else:
    # 2. Pré-processamento do texto
    # Converte tudo para minúsculas e remove pontuação.
    log_limpo = log.lower().translate(str.maketrans('', '', string.punctuation))
    
    # 3. Divide o texto em uma lista de palavras
    palavras = log_limpo.split()

    # 4. Usa o Counter para contar quantas vezes cada palavra aparece
    contagem_palavras = Counter(palavras)

    # 5. Exibe o resultado de forma organizada
    print("\n--- Contagem de Palavras ---")
    for palavra, contagem in contagem_palavras.items():
        print(f"'{palavra}': {contagem} vez(es)")