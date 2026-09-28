"""
Nested if adalah if statement yang berada di dalam if statement lainnya.
"""
# contoh 
bilangan = 10 
if (bilangan % 2 == 0):
    if (bilangan > 0):
        print(f"bilangan {bilangan} adalah genap positif")
    else:
        print(f"bilangan {bilangan} adalah genap negatif")
elif (bilangan % 2 != 0):
    if (bilangan > 0):
        print(f"bilangan {bilangan} adalah ganjil positif")
    else:
        print(f"bilangan {bilangan} adalah ganjil negatif")
else :
    print(f"bilangan {bilangan} adalah  nol")
    
    
# program untuk menghitung diskon belanjaan
total_belanja = 29000
# diskon = 0

print(f"\nTotal belanja kamu adalah {total_belanja}")
if (total_belanja > 70000):
    diskon = total_belanja * 0.2
    print(f"Kamu mendapat diskon sebesar 20% yaitu {diskon}")
else:
    if (total_belanja > 50000):
        diskon = total_belanja * 0.1
        print(f"Kamu mendapat diskon sebesar 10% yaitu {diskon}")
    else : 
        if (total_belanja > 30000):
            diskon = total_belanja * 0.05
            print(f"Kamu mendapat diskon sebesar 5% yaitu {diskon}")
        else : 
            diskon = 0; 
            print(f"Kamu tidak mendapat diskon, karena total belanja kamu kurang dari 30000")
    
print(f"Total yang harus di bayar adalah {total_belanja - diskon}")



""" 
Latihan membuat kalkulator sederhana menggunakan nested if statement, dimana program akan meminta input dari pengguna berupa 2 angka dan operator (+, -, *, /) dan mengembalikan hasil dari operasi tersebut. 
- ada 3 inputan dari pengguna, yaitu angka pertama, operator, dan angka kedua
- cek input operator, jika operator adalah + maka lakukan penjumlahan, jika operator adalah - maka lakukan pengurangan, jika operator adalah * maka lakukan perkalian, jika operator adalah / maka lakukan pembagian.
    - hasilnya tampilkan ke layar dengan format "Hasil dari {angka pertama} {operator} {angka kedua} = {hasil}"
- di dalam pembagian, cek apakah angka kedua adalah 0, jika iya maka tampilkan pesan error "Tidak bisa membagi dengan 0", jika tidak maka lakukan pembagian.
- jika operator bukan salah satu dari +, -, *, / maka tampilkan pesan error "Operator tidak valid (hanya bisa +, -, *, /)"
"""