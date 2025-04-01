import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('/home/rodrigo/projetos/scrapy/data/shopee.db')

df = pd.read_sql_query("SELECT * FROM shopee_items", conn)

conn.close()

st.title('Pesquisa de Mercado - Imóveis na olx do estado do Rio de Janeiro')

st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

total_itens = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_itens)

unique_municipality = df['municipality'].nunique()
col2.metric(label="Número de Cidades", value=unique_municipality)

st.subheader('Cidades mais encontradas')
col1, col2 = st.columns([4, 2])
top_pages_municipality = df['municipality'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_pages_municipality)
col2.write(top_pages_municipality)

st.subheader('Categoria mais encontradas')
col1, col2 = st.columns([4, 2])
top_pages_category = df['category'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_pages_category)
col2.write(top_pages_category)
