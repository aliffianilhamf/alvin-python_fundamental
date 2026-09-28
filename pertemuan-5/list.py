print("Membuat list")
my_list = ["apel", "jeruk", "pisang"]
my_list2 = [1, 2, 3, 4, 5]
my_list3 = [1, "apel", 2.5, True] 

print(my_list)
print(my_list2)
print(my_list3)

print("\nMengakses list")
print(f"Isi dari my_list[0] = {my_list[0]}")
print(f"Isi dari my_list[2] = {my_list[2]}")
print(f"Isi dari my_list2[-1] = {my_list2[-1]}")
print(f"Isi dari my_list2[-3] = {my_list2[-3]}")

print(f"\nMengakses list menggunakan slicing")
print(f"Isi dari my_list3[0:2] = {my_list3[0:2]}")
print(f"Isi dari my_list3[1:] = {my_list3[1:]}")
print(f"Isi dari my_list3[:3] = {my_list3[:3]}")


""" 
Latihan List
my_list4 = ["Ilham", 0, 100, 33, 2.5, "Alip", True, False, 3.14, "Python"]

1. Tampilkan item ke 4 dari my_list4
2. Tampilkan False dengan menggunakan index negatif
3. Tampilkan item ke 2 sampai ke 5 dari my_list4
4. Tampilkan item ke 3 sampai terakhir dari my_list4
5. Tampilkan item ke 1 sampai ke 4 dari my_list4
"""

print(f"\nModifikasi list")
nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"] 
print(f"Isi dari nama_hari = {nama_hari}")
nama_hari[-1] = "Friday"
print(f"Isi dari nama_hari setelah diubah = {nama_hari}")
nama_hari[2] = "Wednesday"
print(f"Isi dari nama_hari setelah diubah = {nama_hari}")
nama_hari[0:2] = ["Monday", "Tuesday"]
print(f"Isi dari nama_hari setelah diubah = {nama_hari}")


print(f"\nMenambahkan item ke list") 
# append -> menambahkan item ke akhir list 
print(f"Isi dari nama_hari = {nama_hari}")
nama_hari.append("Saturday")
print(f"Isi dari nama_hari setelah ditambahkan = {nama_hari}")
nama_hari.append("Sunday")
print(f"Isi dari nama_hari setelah ditambahkan = {nama_hari}")

# insert -> menambahkan item ke list pada index tertentu
numbers = [1, 4, 6, 7, 8]
print(f"\nIsi dari numbers = {numbers}")
numbers.insert(1, "Nana")
print(f"Isi dari numbers setelah ditambahkan = {numbers}")
numbers.insert(3, "Alip")
print(f"Isi dari numbers setelah ditambahkan = {numbers}")

hari = ['senin', 'selasa', 'rabu']
bulan = ['januari', 'februari', 'maret']
print(f"\nIsi dari hari = {hari}")
hari.extend(bulan)
print(f"Isi dari hari setelah ditambahkan = {hari}")
print(f"\nIsi dari bulan = {bulan}")


"""" 
months = ["Januari",  "April", "Mei", , "September", "Oktober", "November"]
1. Lengkapi list months dengan bulan yang belum ada menggunakan bhs inggris 
2. ubah yang maasih berbahasa indonesia menjadi bahasa inggris juga

"""

print(f"\nMenghapus item dari list")
# pop -> menghapus item dari list berdasarkan index , kalau tidak diisi maka akan menghapus item terakhir
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(f"Isi dari months = {months}")
months.pop() # akan menghapus item terakhir dari list
print(f"Isi dari months setelah dihapus = {months}")
months.pop(1) # akan menghapus item ke 2 dari list
print(f"Isi dari months setelah dihapus = {months}")
months.pop(3) # akan menghapus item ke 4 dari list
print(f"Isi dari months setelah dihapus = {months}")


# remove -> menghapus item dari list berdasarkan value
months.remove("March") # akan menghapus item "March" dari list
print(f"\nIsi dari months setelah dihapus = {months}")
months.remove("October") # akan menghapus item "October" dari list
print(f"Isi dari months setelah dihapus = {months}")


print(f"\nLooping pada list")
my_list4 = [100, 200, 300, 400, 500]
for item in my_list4:
    print(f"Isi dari item = {item}")

print(f"\nLooping pada list dengan index")
index = 0
for item in my_list4:
    print(f"Isi dari indeks-{index} = {item}")
    index += 1
    
print() 
for i in range(len(my_list4)):
    print(f"Isi dari indeks-{i} = {my_list4[i]}")
    
print() 
for index, item in enumerate(my_list4):
    print(f"Isi dari indeks-{index} = {item}")
    
    
print(f"\nLooping pada list dengan while")
n = 0 
while n < len(my_list4):
    print(f"Isi dari indeks-{n} = {my_list4[n]}")
    n += 1
    
    
""" 
mahasiswa = ["Andi", "Joko", "Pardi", "Aziz"]
1. Looping  (for & while) dapatkan indeks dan valuenya

nilai = [60, 70, 75, 99, 90, 89, 99, 87]
2. buat list kosong bernama nilai_lulus 
3. gunakan looping untuk memeriksa setiap nilai, jika lebih besar atau sama dengan 80, masukkan nilai ke dalam nilai_lulus
4. tampilkan nilai lulus

kontak_kotor = ["Andi", "Budi", "Andi", "Siti", "Budi", "Dewi", "Siti"]
5. buat list kosong bernama kontak_bersih
6. gunakan looping untuk mengiterasi daftar kontak_kotor, cek apakah nama belum ada di kontak bersih, jika belum, masukkan ke kontak bersih,kalau sudah, tidak perlu di masukkan 
7. cetak isi kontak_bersih
"""

print(f"\nList Comprehension")
numbers = [1, 2, 3, 4, 5]
pangkat_numbers = []
for number in numbers:
    pangkat_numbers.append(number ** 2)
    
print(f"Isi dari pangkat_numbers = {pangkat_numbers}")

pangkat_numbers_comp = [number ** 2 for number in numbers]
print(f"Isi dari pangkat_numbers_comp = {pangkat_numbers_comp}")

number2 = [ 100, 121, 144, 169, 196]
numbers_ganjil = [number for number in number2 if number % 2 == 1]
numbers_genap = [number ** 5 for number in number2 if number % 2 == 0]
print(f"Isi dari numbers_ganjil = {numbers_ganjil}")
print(f"Isi dari numbers_genap = {numbers_genap}")

celcius = [0, 10, 20, 30, 40] 
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
reamur = [((4/5) * temp) for temp in celcius]
print(f"Isi dari fahrenheit = {fahrenheit}")
print(f"Isi dari reamur = {reamur}")

""" 
celcius = [0, 10, 20, 30, 40]
1. Buat list comprehension untuk konversi ke fahrenheit
    fahrenheit = [......]
    print(fahrenheit)

id_karyawan = [102, 105, 201, 304, 307, 408, 511]
2. Buat list comprehension dengan if di akhir untuk id genap
    id_genap = [.......]
    print(id_genap)
    
data_sensor = [20, 75, 45, 110, 15]
3. Buat list comprehension untuk menentukan jarak detkat atau aman, jika jarak kurang dari 50 berarti DEKAT, selain itu, AMAN 
    status_objek = [.......]
    print(status_objek)

"""