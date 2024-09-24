def login(userPin, inputPin):
    for i in range(3):
        if int(userPin) == int(inputPin):
            return True
        return False

def tarikTunai(saldo, jumlahPenarikan):
    if saldo > 0 and saldo > jumlahPenarikan:
        saldo -= jumlahPenarikan
        
        return f"Penarikan berhasil, saldo anda tersisa{saldo}"
    else:
        return "Saldo anda tidak cukup"
    
def printSaldo(saldo):
    return f"Saldo anda tersisa{saldo}"
    
def main():
    userPin = int(123456)
    saldo = int(100000)
    print("Selamat datang di ATM Tel-U PWT")
    inputPin = int(input("Masukkan PIN anda:"))
    if login(userPin, inputPin):
        print("Login berhasil")
        while True:
            penarikan = int(input("Jumlah saldo yang ingin ditarik:"))
            tarikTunai(saldo, penarikan)
            
main()
            