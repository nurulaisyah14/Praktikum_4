# Minta pengguna untuk memasukkan tiga bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

# Inisialisasi variabel untuk bilangan terbesar
bilangan_terbesar = bilangan1

# Periksa apakah bilangan kedua lebih besar dari bilangan_terbesar
if bilangan2 > bilangan_terbesar:
    bilangan_terbesar = bilangan2

# Periksa apakah bilangan ketiga lebih besar dari bilangan_terbesar
if bilangan3 > bilangan_terbesar:
    bilangan_terbesar = bilangan3

# Tampilkan bilangan terbesar 
print("Bilangan terbesar adalah:", bilangan_terbesar)
