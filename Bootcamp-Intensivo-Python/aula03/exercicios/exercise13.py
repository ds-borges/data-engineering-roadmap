### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.


import json

records_pages = input("Entre com os dados da pagina: ")

try:
    if not records_pages:
        raise ValueError("Dados vazio !!")
    
    if "=" in records_pages:
        stripped_records = records_pages.split("=")[1].strip()
    else:
        stripped_records = records_pages.strip()
    
    if "'" in stripped_records:
        stripped_records = stripped_records.replace("'", '"')
    
    records_api = json.loads(stripped_records)
            
except ValueError as e:
    print(f"Error: {e}")
else:
    result_api = []
    index=0
    while True:
        if not records_api[index]:
            break
        actual_page=records_api[index]      
        result_api.append(actual_page)
        index +=1 
    
    # 6. Exibe o resultado final
    print("\nOs dados consumidos foram:")
    print(f"{result_api}")