import pandas as pd
from modulos.database import engine


def carregar_dados(month):
    query = f"select * from {month}"
    return pd.read_sql(query, engine)
