import pandas as pd 
import plotly.express as px 
import streamlit as st 

car_data = pd.read_csv('/workspaces/Data-analyst-Portafolio/Notebooks/vehicles_us.csv')
hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto CSV')
    
    fig = px.histogram(car_data, x = 'odometer')
    
    st.plotly_chart(fig, use_container_width=True)

    