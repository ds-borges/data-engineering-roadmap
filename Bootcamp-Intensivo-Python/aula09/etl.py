import glob
import os
from typing import List

import pandas as pd
from utils_log import log_decorator

# Uma função de extract que lê e consolida os json


@log_decorator
def extrair_dados_e_consolidade(pasta: str) -> pd.DataFrame:
    arquivo_json = glob.glob(os.path.join(pasta, "*.json"))
    df_lista: List = [pd.read_json(arquivo) for arquivo in arquivo_json]
    df_total: List = pd.concat(df_lista, ignore_index=True)
    return df_total


@log_decorator
# Uma função que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


@log_decorator
# Uma função que dá load em csv ou parquet
def carregar_dados(df: pd.DataFrame, format_saida: List):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    if "csv" in format_saida:
        df.to_csv("dados.csv", index=False)
    if "parquet" in format_saida:
        df.to_parquet("dados.parquet", index=False)


@log_decorator
# pipline final que consolida as outras
def pipeline_calcular_kpi_de_vendas_consolidados(pasta: str, formato_de_saida: List):
    data_frame = extrair_dados_e_consolidade(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)
