import pandas as pd 
import plotly.express as px 
import streamlit as st 


car_data = pd.read_csv('vehicles_us.csv')
st.header('Proyecto 7 - Herramientas de Desarrollo de Software')

if st.checkbox('Generar Gráfico de Dispersión'):
    st.write('Cantidad de Kilometros por Precio de Vehículos')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig)  
    
if st.checkbox('Generar Gráfico de Barras'):
    st.write('Cantidad de Vehículos por Tipo')
    fig = px.bar(car_data, x = 'type', pattern_shape='type', color='type', color_discrete_sequence=px.colors.qualitative.Set1,)
    st.plotly_chart(fig)
    
if st.checkbox('Generar Histograma'):
    st.write('Condiciones de los Vehículos')
    fig = px.histogram(car_data, x = 'model_year', color='condition', histnorm='percent', opacity=0.75)
    st.plotly_chart(fig, use_container_width=True) 