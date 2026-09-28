# function -- void 
counter = 0
def sapa():
    global counter
    counter += 1
    print("Hello, selamat datang di kelas Python!")

sapa()
print(f"Fungsi sapa() telah dipanggil sebanyak {counter} kali")
# function -- return 
def hasil_jumlah():
    a = 10
    b = 20
    print(f"Nilai a = {a}, Nilai b = {b}")
    return a + b

result = hasil_jumlah()
print(f"Hasil dari fungsi hasil_jumlah() = {result}")
print(f"Hasil dari fungsi hasil_jumlah() = {hasil_jumlah()}")

# parameter
def hasil_jumlah_parameter(a, b):
    print(f"Nilai a = {a}, Nilai b = {b}")
    return a + b

# hasil_jumlah_parameter(1,2)
print(f"Hasil dari fungsi hasil_jumlah_parameter() = {hasil_jumlah_parameter(1,2)}")

def sapa_tamu(nama_tamu):
    print(f"Hello {nama_tamu}, selamat datang di kelas Python!")
    
    
sapa_tamu("Alvin")
sapa_tamu("Budi")
sapa_tamu("Caca")

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# c = []
# # c = a + b
# for i in range(len(a)):
#     c.append(hasil_jumlah_parameter(a[i], b[i])) 
    
# print(f"Hasil dari fungsi hasil_jumlah_parameter() dengan list a dan b = {c}")

def segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    return luas


""" 
Latihan soal 1 
- cari volume dari prisma segitiga dengan rumus volume = 1/2 * a * t * p, dimana a = alas, t = tinggi, p = panjang prisma
- buatlah fungsi untuk menghitung luas segitiga dengan rumus luas = 1/2 * a * t, dimana a = alas, t = tinggi

Latihan soal 2
- cari volumed dari limas segitiga dengan rumus volume = 1/3 * luas_alas * tinggi, dimana luas_alas = 1/2 * a * t, a = alas, t = tinggi
- cari luas alas dengan fungsi luas segitiga yang telah dibuat pada soal 1

Latihan soal 3
- Buat fungsi untuk menampilkan hasil pangkat 2 dari sebuah list angka, misal list = [1, 2, 3, 4, 5], maka hasilnya = [1, 4, 9, 16, 25]

Latihan 4
- Buat fungsi yang menerima parameter panjang dan lebar, lalu hitung luas persegi panjang dengan rumus luas = panjang * lebar, dan keliling = 2 * (panjang + lebar), lalu tampilkan hasilnya dalam format string, misal "Luas persegi panjang = 20, Keliling persegi panjang = 18"
"""


print()
def sapa_tamu_2(nama="Ilham", alamat="Semarang"):
    print(f"Hello {nama}, selamat datang di kelas Python! Alamat anda = {alamat}")
    
# dengan parameter komplit 
sapa_tamu_2("Alvin", "Jakarta")
# dengan parameter default
sapa_tamu_2("Budi")

# keyword paramater 
print()
sapa_tamu_2(nama="Caca", alamat="Bandung")
sapa_tamu_2(alamat="Bandung")
sapa_tamu_2(alamat="Bandung", nama="Dodi")