urutan=[]
def faktorial(n):
    global urutan
    if n == 0 or n == 1:
        return [1]
    else:
        hasil= n * faktorial(n - 1)
        urutan.append(hasil)
    
def main():
    global urutan
    n=4
    faktorial(n)
    urutan.sort(reverse=True)
    return urutan

main()