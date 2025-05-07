import math_operations

from math_operations import celsius_ke_kelvin, keliling_persegi_panjang

print("=== PERHITUNGAN GEOMETRI ===")
sisi = 4
panjang = 10
lebar = 5
jari_jari = 7

print(f"Luas Persegi (sisi={sisi}): {math_operations.luas_persegi(sisi)}")
print(f"Keliling Persegi (sisi={sisi}): {math_operations.keliling_persegi(sisi)}")
print(f"Luas Persegi Panjang (p={panjang}, l={lebar}): {math_operations.luas_persegi_panjang(panjang, lebar)}")
print(f"Keliling Persegi Panjang (p={panjang}, l={lebar}): {keliling_persegi_panjang(panjang, lebar)}")
print(f"Luas Lingkaran (r={jari_jari}): {math_operations.luas_lingkaran(jari_jari):.2f}")
print(f"Keliling Lingkaran (r={jari_jari}): {math_operations.keliling_lingkaran(jari_jari):.2f}")

print("\n=== KONVERSI SUHU ===")
cel = 25
print(f"{cel}°C ke Fahrenheit: {math_operations.celsius_ke_fahrenheit(cel):.2f}°F")
print(f"{cel}°C ke Kelvin: {celsius_ke_kelvin(cel):.2f} K")
