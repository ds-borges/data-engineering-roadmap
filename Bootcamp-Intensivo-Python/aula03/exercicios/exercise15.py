### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

"""
Instruções de uso:
1. Ao executar o script, ele pedirá para você inserir uma lista de dados.
2. A entrada deve ser uma string em formato JSON, como uma lista de números.
3. O script irá processar os itens da lista até encontrar o valor '25', que é
   o critério de parada.
4. Os itens processados antes do critério de parada serão exibidos.
5. Se o critério de parada não estiver na lista, uma mensagem de aviso será mostrada.

Exemplo de entrada:
dados = [10, 25, 30, -1, 45, 50, 60]
[10, 25, 30, -1, 45, 50, 60]

Saída esperada:
O critério de parada foi encontrado na posição -1:
Os números registrados antes foram: [10, 25, 30]
"""

import json

# Pede a entrada dos dados da lista em formato JSON
item_list = input("Entre com os dados da pagina: ")

# Define o valor de parada, que neste caso é 25
spy = -1

try:
    if not item_list:
        raise ValueError("Dados vazio !!")
    
    # Prepara a string de entrada para ser lida como JSON
    if "=" in item_list:
        stripped_list = item_list.split("=")[1].strip()
    else:
        stripped_list = item_list.strip()
    
    if "'" in stripped_list:
        stripped_list = stripped_list.replace("'", '"')
    
    if ',' not in stripped_list:
        raise ValueError("Formato de entrada invalido")
    
    # Converte a string JSON para uma lista Python
    records_list = json.loads(stripped_list)
    
except ValueError as e:
    print(f"Error: {e}")
else:
    # A lógica de processamento começa aqui, após a validação da entrada
    result_api = []
    index = 0
    
    # Verifica se o valor de parada existe na lista antes de iniciar o processamento
    if spy in records_list:
        # Loop infinito que será interrompido pela condição de parada
        while True:
            # Verifica se o item atual na lista é o valor de parada
            if records_list[index] == spy:
                # Interrompe o loop ao encontrar o valor de parada
                break
            
            # Pega o item atual e o adiciona à lista de resultados
            current_item = records_list[index]      
            result_api.append(current_item)
            
            # Avança para o próximo item
            index += 1
        
        # Exibe os resultados após o loop ser interrompido
        print(f"\nO critério de parada foi encontrado na posição {index+1}:")
        print(f"Os números registrados antes foram: {result_api}")
        
    else:
        # Mensagem exibida se a condição de parada não for encontrada
        print("O critério de parada não está nesta lista !!")