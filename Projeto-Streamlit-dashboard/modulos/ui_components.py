import streamlit as st

CARD_STYLE = """
<div style="
    padding: 16px;
    border-radius: 8px;
    background-color: #111827;
    border: 1px solid #374151;
    width: 100%;
    height: 140px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 16px;
">
    <h3 style="margin: 0; color: #e5e7eb;
    font-size: 18px; line-height:1.3;">{titulo}</h3>
    <p style="margin: 8px 0 0; color: #9ca3af; font-size: 24px;">
        {valor}
    </p>
</div>
"""


def card(col, titulo, valor):
    with col:
        st.markdown(
            CARD_STYLE.format(titulo=titulo, valor=valor),
            unsafe_allow_html=True,
        )
