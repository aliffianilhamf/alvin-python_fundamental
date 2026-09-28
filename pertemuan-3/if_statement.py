""" 
If Statement adalah pernyataan bersyarat yang digunakan untuk mengeksekusi blok kode tertentu jika kondisi yang diberikan bernilai True. Jika kondisi bernilai False, blok kode tersebut akan dilewati dan program akan melanjutkan ke pernyataan berikutnya.
"""

diskon = 0 
total_belanja = 100000

# beri kondisi, jika total belanja itu lebih dari 100000, maka akan diberikan diskon sebesar 10% 
# if (total_belanja > 100000): 
#     diskon = total_belanja * 0.1 
    
# if (total_belanja <= 100000):
#     print(f"Kamu tidak mendapat diskon, karena total belanja kamu kurang dari 100000")




# dengan if else 
if (total_belanja > 100000): 
    diskon = total_belanja * 0.1 
else:
    print(f"Kamu tidak mendapat diskon, karena total belanja kamu kurang dari 100000")
    
print(f"Total Belanja: {total_belanja} dan Diskon: {diskon}")
print("Akhir dari program\n")



# contoh 2 
bilangan = 0
# kita ingin mencari apakah suati bilangan itu genap dan positif 
# if ((bilangan % 2 == 0) and (bilangan > 0)):
#     print(f"bilangan {bilangan} adalah genap positif")
    
# if ((bilangan % 2 == 0) and (bilangan < 0)):
#     print(f"bilangan {bilangan} adalah genap negatif")
    
# if ((bilangan % 2 != 0) and (bilangan > 0)):
#     print(f"bilangan {bilangan} adalah ganjil positif")
    
# if ((bilangan % 2 != 0) and (bilangan < 0)):
#     print(f"bilangan {bilangan} adalah ganjil negatif")
    
# if (bilangan == 0):
#     print(f"bilangan {bilangan} adalah  nol")

# elif
if ((bilangan % 2 == 0) and (bilangan > 0)):
    print(f"bilangan {bilangan} adalah genap positif")
elif ((bilangan % 2 == 0) and (bilangan < 0 )):
    print(f"bilangan {bilangan} adalah genap negatif")
elif ((bilangan % 2 != 0) and (bilangan > 0)):
    print(f"bilangan {bilangan} adalah ganjil positif")
elif ((bilangan % 2 != 0) and (bilangan < 0)):
    print(f"bilangan {bilangan} adalah ganjil negatif")
else : 
    print(f"bilangan {bilangan} adalah  nol")
    

"""
Latihan Soal 1:
Buatlah sebuah program yang meminta input dari pengguna berupa umur. 
- jika umur lebih dari sama dengan 18,maka print "Kamu sudah bisa nyoblos"
- jika umur kurang dari 18, maka print "Kamu belum bisa nyoblos"

Latihan Soal 2:
Buatlah program yang meminta input dari pengguna berupa angka
- cek apakah angka tersebut positif, negatif, atau nol.

Latihan Soal 3:
Buat program untuk mencari number terbesar dari 3 angka yang dimasukkan oleh pengguna.
- tampilkan hasilnya dengan format "angka terbesar adalah: {angka_terbesar}" 


Latihan Soal 4:
Buatlah program untuk menghitung konversi suhu dari Celcius ke Fahrenheit, Celcius ke reamur, dan celcius ke Kelvin. 
- Buat inputan dari pengguna berupa suhu dalam Celcius
- print pilihan tujuan konversi, misal : 
    Pilih Tujuan Konversi
    1. Celcius ke Fahrenheit
    2. Celcius ke Reamur
    3. Celcius ke Kelvin
- jika pengguna memilih 1, maka lakukan konversi ke Fahrenheit dan tampilkan hasilnya
    - rumus konversi Celcius ke Fahrenheit = (Celcius * 9/5) + 32
    - contoh hasil konversi: 37 "Celcius = 98.6 Fahrenheit"
- jika pengguna memilih 2, maka lakukan konversi ke Reamur dan tampilkan hasilnya
    - rumus konversi Celcius ke Reamur = Celcius * 4/5
    - contoh hasil konversi: 37 "Celcius = 29.6 Reamur"
- jika pengguna memilih 3, maka lakukan konversi ke Kelvin dan tampilkan
    - rumus konversi Celcius ke Kelvin = Celcius + 273.15
    - contoh hasil konversi: 37 "Celcius = 310.15 Kelvin"
- jika pilihan tidak valid, maka tampilkan "Pilihan tidak valid, silahkan pilih 1, 2, atau 3"

"""