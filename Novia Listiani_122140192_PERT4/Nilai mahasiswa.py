# Data Mahasiswa
mahasiswa = [
    {"nama": "Novia Listiani", "nim": "12345", "nilai_uts": 75, "nilai_uas": 80, "nilai_tugas": 85},
    {"nama": "Faradysa", "nim": "12346", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 75},
    {"nama": "Cici", "nim": "12347", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 90},
    {"nama": "Dina", "nim": "12348", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 65},
    {"nama": "Anvita", "nim": "12349", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 100}
]

# Menghitung nilai akhir dan grade
for mhs in mahasiswa:
    nilai_akhir = mhs["nilai_uts"] * 0.3 + mhs["nilai_uas"] * 0.4 + mhs["nilai_tugas"] * 0.3
    mhs["nilai_akhir"] = nilai_akhir
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif 70 <= nilai_akhir < 80:
        mhs["grade"] = "B"
    elif 60 <= nilai_akhir < 70:
        mhs["grade"] = "C"
    elif 50 <= nilai_akhir < 60:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

# Menampilkan hasil
print(f"{'Nama':<10}{'NIM':<10}{'Nilai Akhir':<15}{'Grade'}")
for mhs in mahasiswa:
    print(f"{mhs['nama']:<10}{mhs['nim']:<10}{mhs['nilai_akhir']:<15}{mhs['grade']}")

# Mencari nilai tertinggi dan terendah
tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print("\nNilai tertinggi:")
print(f"Nama: {tertinggi['nama']}, Nilai Akhir: {tertinggi['nilai_akhir']}, Grade: {tertinggi['grade']}")

print("\nNilai terendah:")
print(f"Nama: {terendah['nama']}, Nilai Akhir: {terendah['nilai_akhir']}, Grade: {terendah['grade']}")
