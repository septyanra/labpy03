print("Program Menampilkan Bilangan Terbesar dari Bilangan n")

n = 1
max = 0
while n !=0:
    if n > max:
        max = n
    n = int(input("Masukkan bilangan : "))
    if n == 0:
        break
print("Nilai terbesar adalah : ", max)
