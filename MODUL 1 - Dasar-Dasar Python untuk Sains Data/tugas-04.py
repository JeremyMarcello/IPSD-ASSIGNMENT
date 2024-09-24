import pandas as pd

data = pd.read_csv("D:/Data/Kuliah/SEMESTER 3/INFRASTRUKTUR DAN PLATFORM UNTUK SAINS DATA/PRAKTIKUM/IPSD-ASSIGNMENT/MODUL 1 - Dasar-Dasar Python untuk Sains Data/siswa_nilai.csv")
print(data)

nilaiSiswa = data.to_dict(orient='list')
print(nilaiSiswa)
print()

nilai = nilaiSiswa.get('Nilai', [])
nama = nilaiSiswa.get('Nama Siswa', [])

if nilai:
    rata = sum(nilai) / len(nilai)
    rataAll = round(rata, 2)
    print(f"Rata-rata nilai adalah: {rataAll}")
    nilaiMax = max(nilai)
    nilaiMin = min(nilai)
    print(f"Nilai tertinggi adalah: {nilaiMax}")
    print(f"Nilai terendah adalah: {nilaiMin}")
else:
    print("Nilai tidak ada")