import streamlit as st

def konversi_celsius(celsius):
    fahrenheit = (celsius * 9/5) + 32
    reamur = celsius * 4/5
    kelvin = celsius + 273.15
    return fahrenheit, reamur, kelvin

st.title("Konversi Suhu Celsius")

nilai_celsius = st.number_input("Masukkan nilai Celsius:", value=
