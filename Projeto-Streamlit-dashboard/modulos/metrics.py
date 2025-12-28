def gasto_total(df):
    return f"{df['valor'].sum():.2f}"


def categoria_mais_cara(df):
    return df.groupby("categoria")["valor"].sum().idxmax()


def quantidade_compras(df):
    return len(df)


def valor_por_categorias(df):
    return df.groupby("categoria")["valor"].sum().reset_index(name="valor_total")


def valor_por_pessoas(df):
    return df.groupby("fontes")["valor"].sum().reset_index(name="valor_total")
