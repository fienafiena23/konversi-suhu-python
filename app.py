import streamlit as st

def konversi_celsius(celsius):
    fahrenheit = (celsius * 9/5) + 32
    reamur = celsius * 4/5
    kelvin = celsius + 273.15
    return fahrenheit, reamur, kelvin

st.title("Konversi Suhu Celsius")

nilai_celsius = st.number_input("Masukkan nilai Celsius:", value=0.0)

F, R, K = konversi_celsius(nilai_celsius)

st.write("---")
st.write(f"**Fahrenheit:** {F:.2f} °F")
st.write(f"**Reamur:** {R:.2f} °R")
st.write(f"**Kelvin:** {K:.2f} K")
