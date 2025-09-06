### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários, filtrar aqueles que têm um campo específico faltando

'''
Instruções:
    O programa aceita uma lista de dicionários no formato JSON.
    As chaves obrigatórias são 'id', 'nome', 'email' e 'idade'.

Exemplos de entrada:
    usuarios = [
    {"id": 1, "nome": "Alice", "email": "alice@email.com", "idade": 25},
    {"id": 2, "nome": "Bob", "email": None, "idade": 30},
    {"id": 3, "nome": "Charlie", "idade": 35, "telefone": "9999-9999"},
    {"id": 4, "nome": "Diana", "email": "diana@email.com", "idade": 40},
    {"id": 5, "nome": "Eve", "email": "", "idade": 28}]

Retorno:
    Uma nova lista contendo apenas os dicionários que passaram na validação.
'''

import json

log = input("Entre com as informações dos usuários: ")

# Define as chaves obrigatórias em um conjunto.
chaves_obrigatorias = {"id", "nome", "email", "idade"}

try:
    # 1. Trata a entrada do usuário para o formato JSON.
    if "=" in log:
        log_users = log.split("=")[1].strip()
    else:
        log_users = log.strip()
    
    # Substitui as aspas simples por duplas se tiver.
    if "'" in log:
        log_users = log_users.replace("'", '"')
    
    # Substitui 'None' por 'null' para ser compatível com JSON se tiver como 'None'.
    if "None" in log:
        log_users = log_users.replace("None", 'null')

    # 2. Converte a string JSON para uma lista de dicionários Python.
    log_dictionary = json.loads(log_users)

    user_okay = []  # Lista para armazenar os usuários válidos.
    
    # 3. Percorre cada dicionário na lista.
    for usuario in log_dictionary:
        is_valido = True  # Flag para checar a validade do usuário.
        
        # 4. Percorre as chaves obrigatórias para validação.
        for chave in chaves_obrigatorias:
            # Se a chave não existe OU o valor é nulo/vazio, o usuário não é válido.
            if chave not in usuario or not usuario[chave]:
                is_valido = False
                break  # Sai do loop interno, não precisa checar mais.
        
        # 5. Se o usuário passou por todas as checagens, o adiciona à lista final.
        if is_valido:
            user_okay.append(usuario)

# Captura erros comuns de formato JSON ou chaves ausentes.
except (ValueError, IndexError, KeyError, TypeError) as e:
    print(f"\nErro: Verifique o formato da sua entrada. Detalhes: {e}")

# Bloco executado apenas se o "try" for bem-sucedido.
else:
    print(f"\nUsuários filtrados: {user_okay}")