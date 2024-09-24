prima = []

def cekPrima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def barisPrima(n):
    global prima
    angka = 1
    for i in range(1, n+1):
        while len(prima) < sum(range(1,i+1)):
            if cekPrima(angka):
                prima.append(angka)
            angka += 1
        print(*prima[-i:])

barisPrima(5) 