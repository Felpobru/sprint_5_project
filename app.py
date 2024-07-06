import pandas as pd
import plotly.express as px
import streamlit as st

file_path = 'vehicles.csv'
df = pd.read_csv(file_path)

st.header("Análise de Dados de Veículos")

build_histogram = st.checkbox('Criar histograma')

if build_histogram:

    st.write('Criando um histograma para o conjunto de dados de veículos')

    fig = px.histogram(df, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:

    st.write('Criando um gráfico de dispersão para o conjunto de dados de veículos')

    fig = px.scatter(df, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
