import pandas as pd 
import plotly.express as px 
import streamlit as st 

car_data = pd.read_csv('vehicles_us.csv')
st.header('Proyecto 7 - Herramientas de Desarrollo de Software')

if st.checkbox('Generar Histograma'):
    st.write('Creación de un histograma para el conjunto CSV')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Generar Gráfico de Dispersión'):
    st.write('Creación de un Gráfico de Dispersión para el conjunto CSV')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig)  