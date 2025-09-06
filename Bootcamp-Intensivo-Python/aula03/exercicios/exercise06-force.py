### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

import string # Importa o módulo 'string' para lidar com pontuação.

repeat = [] # Cria uma lista vazia para armazenar as palavras e suas contagens.

try:
    # Solicita a entrada do usuário.
    log = input("Dê os detalhes da transação: ")
    
    # Converte o texto para minúsculas e remove a pontuação.
    log_clean = log.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Divide a string em uma lista de palavras.
    log_strip = log_clean.split()
    
    # Se a lista de palavras estiver vazia, levanta um erro.
    if not log_strip:
        raise ValueError("String vazia")

# Captura erros do tipo ValueError.
except ValueError as e:
    print(f"Error: {e}")

# Executa se não houver erros no bloco 'try'.
else:
    # Percorre cada palavra na lista de palavras.
    for main_cont, sentence in enumerate(log_strip):
        # Checa se a palavra ainda não foi processada.
        if not sentence in repeat:
            num = 0 # Reinicia o contador para a nova palavra.
            
            # Percorre a lista de palavras novamente para contar as repetições.
            for palavra in log_strip:
                # Se a palavra for igual e ainda não estiver na lista 'repeat', incrementa o contador.
                if sentence == palavra:
                    num += 1
            
            # Adiciona a palavra e sua contagem à lista 'repeat'.
            repeat.append(sentence)
            repeat.append(num)

    # Exibe o resultado de forma organizada.
    print("\nO resultado do processo é:")
    
    # Percorre a lista 'repeat' de 2 em 2 para pegar a palavra e sua contagem.
    for i in range(0, len(repeat), 2):
        palavra = repeat[i]
        contagem = repeat[i + 1]
        print(f"'{palavra}': {contagem} vez(es)")