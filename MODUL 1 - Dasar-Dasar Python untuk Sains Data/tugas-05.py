import random

def tebakAngka():
    angka = random.randint(1, 100)
    batasPercobaan = 5
    percobaan = 0
    batasBawah = 1
    batasAtas = 100
    print("Selamat datang di permainan tebak angka!")
    print("Komputer telah memilih sebuah angka antara 1 hingga 100.")
    print(f"Anda memiliki {batasPercobaan} kesempatan untuk menebaknya.")
    while percobaan < batasPercobaan:
        try:
            tebakan = int(input(f"Tebakan ke-{percobaan + 1}: Masukkan angka Anda (antara {batasBawah} dan {batasAtas}): "))
            if tebakan < batasBawah or tebakan > batasAtas:
                print(f"Angka di luar batas! Silakan masukkan angka antara {batasBawah} dan {batasAtas}.")
                continue
            percobaan += 1
            if tebakan == angka:
                print(f"Selamat! Anda berhasil menebak angka {angka} dengan benar.")
                return
            elif tebakan < angka:
                print("Tebakan Anda terlalu kecil.")
                batasBawah = tebakan + 1
            else:
                print("Tebakan Anda terlalu besar.")
                batasAtas = tebakan - 1
            print(f"Petunjuk: Coba angka antara {batasBawah} dan {batasAtas}.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    print(f"Anda kehabisan kesempatan. Angka yang benar adalah {angka}.")
    print("Permainan selesai. Semoga beruntung lain kali!")

tebakAngka()