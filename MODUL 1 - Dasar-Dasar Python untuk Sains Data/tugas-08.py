def balik_kata(x):
    kata = x.split()
    balik = [kata[::-1] for kata in kata]
    return balik

x = "Nama Saya Jeremy"
hasil = balik_kata(x)
print(hasil)