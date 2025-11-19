def konversi_celsius(celsius):
    """Fungsi untuk mengkonversi suhu dari Celsius ke skala lain."""

    # Konversi ke Fahrenheit: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32

    # Konversi ke Reamur: R = C * 4/5
    reamur = celsius * 4/5

    # Konversi ke Kelvin: K = C + 273.15
    kelvin = celsius + 273.15

    # Mengembalikan hasil konversi
    return fahrenheit, reamur, kelvin

# --- Bagian Utama Program ---

# 1. Input nilai Celsius dari pengguna
# Menggunakan float() agar bisa menerima input desimal
nilai_celsius = float(input("Masukkan nilai suhu dalam Celsius (C): "))

# 2. Panggil fungsi konversi
F, R, K = konversi_celsius(nilai_celsius)

# 3. Tampilkan hasil konversi
print("\n--- Hasil Konversi Suhu ---")
print(f"Suhu Awal (Celsius): {nilai_celsius:.2f} °C")
print("-" * 30)
print(f"Fahrenheit (F): {F:.2f} °F")
print(f"Reamur (R): {R:.2f} °R")
print(f"Kelvin (K): {K:.2f} K")