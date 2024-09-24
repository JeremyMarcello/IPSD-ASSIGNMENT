def binarySearch(angka, cari):
    if cari % 2 != 0:
        return f"Nilai {cari} adalah angka ganjil, nilai tidak ditemukan."
    awal = 0
    akhir = len(angka) - 1
    while awal <= akhir:
        tengah = (awal + akhir) // 2
        if angka[tengah] == cari:
            return f"Nilai {cari} ditemukan pada indeks ke-{tengah}."
        elif angka[tengah] > cari:
            akhir = tengah - 1
        else:
            awal = tengah + 1
    return f"Nilai {cari} tidak ditemukan."

angka_genap = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
cari1 = 8
cari2 = 7
print(binarySearch(angka_genap, cari1))
print(binarySearch(angka_genap, cari2))
