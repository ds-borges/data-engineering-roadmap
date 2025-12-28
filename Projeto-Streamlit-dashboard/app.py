import streamlit as st
from modulos.data_loader import carregar_dados
from modulos.graphics import column_fig, pie_fig, table_fig
from modulos.metrics import categoria_mais_cara, gasto_total, quantidade_compras
from modulos.ui_components import card

st.title("Dashboard Financeiro")


@st.cache_data(ttl=300)
def get_df_atual():
    return carregar_dados("current_months_bill")


@st.cache_data(ttl=300)
def get_df_passado():
    return carregar_dados("past_months_bill")


df_atual = get_df_atual()
df_passado = get_df_passado()

(
    row1_col1,
    row1_col2,
) = st.columns(2)
(
    row2_col1,
    row2_col2,
) = st.columns(2)
row3_col1, row3_col2 = st.columns(2)

st.set_page_config(layout="wide")

card(col=row1_col1, titulo="Gasto deste mês", valor=gasto_total(df_atual))
card(col=row1_col2, titulo="Gasto do mês passado", valor=gasto_total(df_passado))

card(col=row2_col1, titulo="Categoria mais cara", valor=categoria_mais_cara(df_atual))
card(col=row2_col2, titulo="Quantidade de compras", valor=quantidade_compras(df_atual))

column_fig(df_atual, row3_col1)
pie_fig(df_atual, row3_col2)

st.subheader("Detalhamento dos gastos")
table_fig(df_atual)
