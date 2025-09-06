### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

"""
Instruções de uso:
1. Ao executar o script, ele pedirá para você inserir os dados de vendas.
2. A entrada deve ser uma lista de dicionários em formato JSON.
3. Certifique-se de que a string JSON esteja bem formatada, usando aspas duplas (")
   para chaves e strings. Aspas simples (') também são aceitas e serão corrigidas
   automaticamente.

Exemplo de entrada:
vendas = [
    {"categoria": "Eletrônicos", "valor": 1200.00},
    {"categoria": "Livros", "valor": 45.50},
    {"categoria": "Eletrônicos", "valor": 250.00},
    {"categoria": "Casa e Jardim", "valor": 89.90},
    {"categoria": "Livros", "valor": 30.00},
    {"categoria": "Casa e Jardim", "valor": 150.20},
    {"categoria": "Eletrônicos", "valor": 750.00},
    {"categoria": "Livros", "valor": 22.50}]
"""

import json

# 1. Pede a entrada dos dados
records = input("Entre com os dados de vendas: ")

try:
    if not records:
        raise ValueError("Entre com os registros de vendas !!")
    
    # 2. Trata a string de entrada para o formato JSON válido
    if "=" in records:
        sales_records = records.split("=")[1].strip()
    else:
        sales_records = records.strip()
    
    # Converte aspas simples para duplas para compatibilidade com JSON
    if "'" in records:
        sales_records = sales_records.replace("'", '"')
    
    # Converte a string JSON para um dicionário Python
    records_dictionary = json.loads(sales_records)
            
except ValueError as e:
    print(f"Error: {e}")
else:
    # 3. Inicializa um dicionário para armazenar o total de vendas por categoria
    sales_by_cattegory = {}
    
    # 4. Itera sobre cada registro de venda
    for sales in records_dictionary:
        cattegory = sales['categoria']
        value_sales = sales['valor']

        # 5. Lógica de agregação: verifica se a categoria já existe no dicionário
        if cattegory in sales_by_cattegory:
            # Se a categoria existe, soma o valor da venda ao total acumulado
            sales_by_cattegory[cattegory] += value_sales
        else:
            # Se não existe, cria a categoria no dicionário com o valor inicial
            sales_by_cattegory[cattegory] = value_sales
    
    # 6. Exibe o resultado final
    print("\nAs vendas por categoria foram:")
    print(f"{sales_by_cattegory}")