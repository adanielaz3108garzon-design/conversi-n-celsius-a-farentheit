import streamlit as st

# Título
st.title("🌡️ Conversor de Temperatura")

# Selección
opcion = st.radio("Seleccione el tipo de conversión:", 
                  ("Celsius ➝ Fahrenheit", "Fahrenheit ➝ Celsius"))

# Lógica de conversión
if opcion == "Celsius ➝ Fahrenheit":
    celsius = st.number_input("Ingrese la temperatura en °C:", value=0.0)
    fahrenheit = (celsius * 9/5) + 32
    st.success(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
else:
    fahrenheit = st.number_input("Ingrese la temperatura en °F:", value=0.0)
    celsius = (fahrenheit - 32) * 5/9
    st.success(f"{fahrenheit:.2f} °F equivalen a {celsius:.2f} °C")
