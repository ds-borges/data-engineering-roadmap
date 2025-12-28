import altair as alt
import plotly.express as px
import streamlit as st
from modulos.metrics import valor_por_categorias, valor_por_pessoas


def column_fig(df, pos):
    with pos:
        st.markdown("### Quanto foi gasto em cada categoria")
        chart = (
            alt.Chart(valor_por_categorias(df))
            .mark_bar(color="#2196F3")
            .encode(
                x=alt.X("categoria:N", sort="-y", title=None),
                y=alt.Y("valor_total:Q", title="Total gasto"),
                tooltip=["categoria", "valor_total"],
            )
            .properties(height=300)
        )
        st.altair_chart(chart, use_container_width=True)


def pie_fig(df, pos):
    with pos:
        st.markdown("### Valor gasto por cada")
        fig = px.pie(
            valor_por_pessoas(df),
            names="fontes",
            values="valor_total",
            hole=0.6,  # deixa em formato de donut
        )
        fig.update_traces(textinfo="percent+label", showlegend=False)  # mostra % e nome
        fig.update_layout(
            height=300,
            showlegend=True,
            margin=dict(l=10, r=0, t=0, b=0),
            paper_bgcolor="#020617",
            plot_bgcolor="#020617",
        )
        st.plotly_chart(fig, use_container_width=True)


def table_fig(df):
    st.dataframe(
        df.sort_values("create_at", ascending=False).drop(columns=["id", "create_at"]),
        use_container_width=True,
        hide_index=True,
        column_config={
            "descrição": st.column_config.Column(width="large"),
            "categoria": st.column_config.Column(width="small"),
            "valor": st.column_config.Column(width="small"),
            "fontes": st.column_config.Column(width="small"),
            "parcelas": st.column_config.Column(width="small"),
        },
    )
