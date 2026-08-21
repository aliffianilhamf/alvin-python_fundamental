"""  
Input adalah method / fungsi bawaan python yg berguna untuk menangkap segala inputtan dari keyboard user
input selalu mengembalikan string
"""

nama_depan = input("Masukkan nama depan anda: ")
print(f"Nama depan saya adalah {nama_depan} (tipe data: {type(nama_depan)})\n")

angka_1 = input("Masukkan angka pertama: ") 

hasil = angka_1 * 2 
print(f"Hasil perkalian angka pertama dengan 2 adalah {hasil} (tipe data: {type(hasil)})\n")

angka_2 = int(input("Masukkan angka kedua: "))
# angka_2 = int(angka_2)
hasil = angka_2 * 2 
print(f"Hasil perkalian angka kedua dengan 2 adalah {hasil} (tipe data: {type(hasil)})\n")


"""  
Latihan soal 1 - menampilkan hasil inputan 
- Buat variable untuk menampung inputan makanan favoritmu 
- Buat variable untuk menampung inputan minuman favoritmu
- Tampilkan hasil inputan makanan dan minuman favoritmu dengan format: "Makanan favorit saya adalah <makanan> dan minuman favorit saya adalah <minuman>"

Latihan soal 2 - sistem kasir sederhana
- Buat variable untuk menampung nama barang, qty dan harga barang dari user 
- hitung total harga barang dengan rumus: total = qty * harga
- Tampilkan hasil total harga barang dengan format: "Total harga <nama_barang> sebanyak <qty> adalah <total>"

Latihan soal 3 - Menghitung luas dan keliling persegi panjang 
- Buat variable untuk menampung panjang dan lebar dari user
- Hitung luas dan keliling persegi panjang dengan rumus: luas = panjang * lebar, keliling = 2 * (panjang + lebar)
- Tampilkan hasil luas dan keliling persegi panjang dengan format: "Luas persegi panjang adalah <luas> dan keliling persegi panjang adalah <keliling>"
"""