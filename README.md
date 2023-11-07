## Struktur Kondisi
- Pada Latihan 1, kita membuat program sederhana dengan input 2 buah bilangan, kemudian
tentukan bilangan terbesar dari kedua bilangan tersebut
menggunakan statement if.

1. Kode ini menggunakan input(), kode meminta pengguna untuk memasukkan dua bilangan bulat.
2. Kode kemudian membandingkan kedua bilangan menggunakan pernyataan if. Jika bilangan1 lebih besar dari bilangan2, maka bilangan_terbesar diatur menjadi bilangan1, jika tidak, maka diatur menjadi bilangan2.
Terakhir, kode mencetak bilangan terbesar ke konsole / terminal.
3. Hasil akhirnya adalah kode ini akan menampilkan bilangan terbesar dari dua bilangan yang dimasukkan oleh pengguna.



- Lalu pada latihan 2, kita membuat program untuk mengurutkan data berdasarkan input sejumlah
data (minimal 3 variable input atau lebih), kemudian tampilkan
hasilnya secara berurutan mulai dari data terkecil.

1. Program ini meminta pengguna memasukkan jumlah data, kemudian pengguna memasukkan data tersebut. Setelah mengumpulkan semua data, program mengurutkan data dari yang terkecil hingga yang terbesar.
2. Hasil akhirnya adalah kode ini akan menerima input dari pengguna, mengurutkan data yang dimasukkan, dan kemudian mencetak hasil pengurutan tanpa desimal.


## Perulangan
- Pada latihan 1, kita membuat program dengan perulangan bertingkat (nested) for yang
menghasilkan output sebagai berikut:

1. Kode ini mencetak pola tabel 10x10 dengan angka yang dihasilkan dari penjumlahan variabel i dan j dalam loop. Setiap baris mencetak hasil penjumlahan i + j, dengan angka-angka tersebut dipisahkan oleh tab ("\t"), dan kemudian mencetak baris baru untuk mengawali baris baru.


- Pada latihan 2, kita membuat program<br>
  ```Tampilkan n bilangan acak yang lebih kecil dari 0.5.<br>
  ```nilai n diisi pada saat runtime<br>
  ```anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya

1. Kode tersebut meminta pengguna memasukkan jumlah n. Jika n lebih besar dari 0, maka kode akan menghasilkan dan mencetak n bilangan acak yang kurang dari 0.5. Jika n tidak lebih besar dari 0, maka kode akan memberi pesan bahwa n harus lebih besar dari 0.
2. Hasil akhirnya adalah kode ini akan mencetak bilangan acak yang kurang dari 0.5 sebanyak n kali sesuai dengan jumlah yang dimasukkan oleh pengguna.


## Tugas Praktikum 2
- Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya. Gunakan statement if.
1. Program akan meminta pengguna untuk memasukkan tiga bilangan: bilangan1, bilangan2, dan bilangan3.
2. Tentukan sebuah variabel bernama "bilangan_terbesar" untuk menyimpan bilangan terbesar.
3.Gunakan pernyataan if dan elif untuk memeriksa kondisi berikut:<br>
Jika bilangan1 lebih besar dari bilangan2 dan bilangan1 lebih besar dari bilangan3, maka bilangan1 adalah bilangan terbesar.<br>
Jika bilangan2 lebih besar dari bilangan1 dan bilangan2 lebih besar dari bilangan3, maka bilangan2 adalah bilangan terbesar.<br>
Jika kedua kondisi di atas tidak terpenuhi, maka bilangan terbesar adalah bilangan3.
4. program akan mencetak bilangan terbesar ke terminal / konsole.





## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir lab2py
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# lab2py” >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add README.md
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
   contoh: lab2py
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository


- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```


- ## Berikut ini bukti pengerjaan-nya
-  praktikum2 (modul 2)(lab2py02)
- ![alt text](?![lab2py02 praktikum2](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/b7f1c747-730c-4694-b746-149fb0e6d621)
raw=true)
-  praktikum3 (modul 3)(lab2py02)
- ![alt text](?![lab2py03 latihan1](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/ddcaf506-fd44-4f4f-992b-68f4b0b4ab75)
raw=true)
- ![alt text](?![lab2py03 latihan2](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/4ecb3369-224a-4873-b00e-d8a1cb85d53a)
raw=true)
- ![alt text](?![lab2py03 program1](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/65968c68-338a-4e07-8f41-d55904ddeff6)
raw=true)
- lab2 struktur kondisi
- ![alt text](?![lab2struktur_conditional latihan1](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/90f5f6d2-b53a-4875-be0b-e6d5ac5adcb4)
raw=true)
- ![alt text](?![lab2struktur_conditional latihan2](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/22e451e1-63c6-4dfa-82c4-2be7fff39a4e)
raw=true)
- lab3 perulangan
- ![alt text](?![lab3perulangan latihan1](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/2bb3b8b2-39a2-470b-9e35-8d82eb72e37d)
raw=true)
- ![alt text](?![lab3perulangan latihan2](https://github.com/nurulaisyah14/Praktikum_4/assets/148174512/e75be301-c1d2-49fb-8cef-349d50e42db9)
raw=true)
