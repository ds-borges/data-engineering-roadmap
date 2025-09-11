from typing import List

from etl import filtrar_produtos_entregue, ler_csv, soma_valor_dos_produtos

path_arquivo = "vendas.csv"

vendas_itens: List[dict]

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregue(lista_de_produtos)
valor_dos_produtos_entregues = soma_valor_dos_produtos(produtos_entregues)

print(f"A soma do valor dos produtos entregues são {valor_dos_produtos_entregues}")
