my_tup = (1, 2, 3, 4, 5)
print(f"Isi dari my_tup = {my_tup}")

# mengakses tuple menggunakan index
print(f"Isi dari my_tup[0] = {my_tup[0]}")
print(f"Isi dari my_tup[2] = {my_tup[2]}")
print(f"Isi dari my_tup[-1] = {my_tup[-1]}")
print(f"Isi dari my_tup[-3] = {my_tup[-3]}")

# misal ingin mengubah isi dari tuple, maka akan error
# my_tup[0] = 10 # akan error karena tuple tidak dapat diubah
# oleh karena itu, kita harus jadikan list dulu, lalu ubah, baru jadikan tuple lagi 
my_tup_list = list(my_tup)
print(f"Isi dari my_tup_list = {my_tup_list}")
updated_tup_list = [number ** 2 for number in my_tup_list]
updated_tuple = tuple(updated_tup_list)
print(f"Isi dari updated_tuple = {updated_tuple}")

print(f"\nUnpacking tuple")
tup_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
# unpacking tuple
*hari1, hari2, hari3, hari4, hari5, hari6 = tup_hari
print(f"Isi dari hari1 = {hari1}")
print(f"Isi dari hari2 = {hari2}")
print(f"Isi dari hari3 = {hari6}")

print(f"\nLooping pada tuple")
for item in tup_hari:
    print(f"Isi dari item = {item}")
    
# jebakan di tuple 
print(f"\nJebakan di tuple")
tup_bulan = ("januari") # bukan tuple, karena tidak ada koma di akhir, sehingga dianggap string
print(f"Isi dari tup_bulan = {tup_bulan}, tipenya = {type(tup_bulan)}")
tup_bulan = ("januari",) 
print(f"Isi dari tup_bulan = {tup_bulan}, tipenya = {type(tup_bulan)}")

# fungsi zip - menggabungkan data dari beberapa iterable menjadi satu iterable yang berisi tuple
print(f"\nFungsi zip")
list1 = [1, 2, 3]
list2 = ["satu", "dua", "tiga"]
zipped = zip(list1, list2)
print(f"Isi dari zipped = {zipped}")
for item in zipped:
    print(f"Isi dari item = {item}")
    
nama_produk = ["Baju", "Celana", "Sepatu"]
harga_produk = [100000, 200000, 300000]
qty = [1, 2, 3]
for nama, harga, count in zip(nama_produk, harga_produk, qty):
    print(f"Nama produk = {nama}, harga produk = {harga}, beli sebanyak = {count}, total harga = {harga * count}")