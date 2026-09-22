#Librerías
import streamlit as st 
from sklearn.linear_model import LinearRegression 
import numpy as np 
#En streamlit vamos a agregar un título para la página web
st.title("Configuracion inicial") 
#Agregamos un textbox en nuestra página web
st.write("Primera prueba de uso de streamlit y ambiente de MA2026") 
#El streamlit me permite ingresar por un slider el parámetro inversión
gasto=st.slider("Seleccine nivel de gasto en publicicdad", 10,200,50) 
#Variables de nuestro modelo
variable_x = np.array([[10], [20], [30], [40],[50]]) 
variable_y = np.array([15,25,35,45,55]) 
#Entrenamiento de nuestro modelo LR
modelo_lr = LinearRegression() 

modelo_lr.fit(variable_x,variable_y) 
#En streamlit tenemos un botón que dice Predecir y al darle click activará las lineas de código del if
if st.button("Predecir"): resultado = modelo_lr.predict([[gasto]])
    st.success(f"Las ventas proyectadas para una inversion de ${gasto} son: ${resultado[0]}")
