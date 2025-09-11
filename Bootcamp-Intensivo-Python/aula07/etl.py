import csv
from typing import List


def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que le um arquivo csv e retorna uma lista
    de dicionarios
    """
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        lista: List = []
        for linha in leitor:
            lista.append(linha)

    return lista


def filtrar_produtos_entregue(lista: List[dict]) -> List[dict]:
    """
    Função que filtra produtos onde entrega = True
    """

    lista_com_produtos_filtrados: List = []

    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def soma_valor_dos_produtos(lista: List[dict]) -> List[dict]:
    """
    Função que calcula o valor dos produtos
    """

    valor_dos_produtos: int = 0

    for produto in lista:
        valor_dos_produtos += int(produto.get("price"))
    return valor_dos_produtos
