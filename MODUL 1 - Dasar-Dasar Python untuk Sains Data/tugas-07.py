coins = [1, 5, 10, 25]
jumlahCoin = 63
kombinasiCoin = []
    
def minimalCoin():
    global kombinasiCoin, coins, jumlahCoin
    coins.sort(reverse=True)
    for coin in coins:
        if jumlahCoin == 0:
            break
        while jumlahCoin >= coin:
            jumlahCoin -= coin
            kombinasiCoin.append(coin)

minimalCoin()
print(f"Jumlah koin minimum yang dibutuhkan: {len(kombinasiCoin)}")
print(f"Koin yang digunakan: {kombinasiCoin}")