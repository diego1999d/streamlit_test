import streamlit as st

st.header('Lanzar una moneda')

# Slider para elegir número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Botón para ejecutar el experimento
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')

