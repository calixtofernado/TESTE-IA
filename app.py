print ("hello world")
# vibecoding - programar copiloto 
import streamlit as st 
import pandas as pd


st.title('minha web page')
st.map()

dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)

# graficos 
st.image('img.png')
st.bar_chart(df, x = 'vendedor', y = 'vendas')

st.map()


