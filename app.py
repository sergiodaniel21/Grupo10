import streamlit as st

# Importa tus laboratorios
import lab1
import lab2
import lab3

# Título de la aplicación
st.title("Laboratorios del Curso")

# Sidebar de navegación
opcion = st.sidebar.selectbox(
    "Selecciona un laboratorio",
    ["Laboratorio 1", "Laboratorio 2", "Laboratorio 3"]
)

# Mostrar el laboratorio correspondiente
if opcion == "Laboratorio 1":
    lab1.mostrar()
elif opcion == "Laboratorio 2":
    lab2.mostrar()
elif opcion == "Laboratorio 3":
    lab3.mostrar()
