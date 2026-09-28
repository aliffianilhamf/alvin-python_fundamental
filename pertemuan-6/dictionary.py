my_dict = {
    # key : value
    "nama": "Alvin",
    "umur" : "18",
    "alamat" : "Jakarta",
}
print(f"Isi dari my_dict = {my_dict}")

print(my_dict.keys())
dict_baru = dict.fromkeys(my_dict.keys())
print(f"Isi dari dict_baru = {dict_baru}")

my_dict2 = {
    10: "sepuluh",
    20: "dua puluh",
    30: "tiga puluh",
}
print(f"Isi dari my_dict2 = {my_dict2}")

my_dict3 = {
    (1, 2): "satu dua",
    (3, 4): "tiga empat",
}
print(f"Isi dari my_dict3 = {my_dict3}")

my_dict4 = dict(nama="Alvin", umur=18, alamat="Jakarta")
print(f"Isi dari my_dict4 = {my_dict4}")

keys = ["nama", "umur", "alamat"]
values = ["Alvin", 18, "Jakarta"]
my_dict5 = dict(zip(keys, values))
print(f"Isi dari my_dict5 = {my_dict5}")


print(f"\nMengakses Dictionary")
print((f"my_dict['nama'] = {my_dict['nama']}"))
print(f"my_dict2[20] = {my_dict2[20]}")
# menggunakan method get() untuk mengakses dictionary
print(f"my_dict.get('alamat') = {my_dict.get('alamat')}")


# mengupdate dictionary
print(f"\nMengupdate Dictionary")
my_dict["nama"] = "Alvin Wijaya"
print(f"Isi dari my_dict setelah diupdate = {my_dict}")
# menggunakan method update() untuk mengupdate dictionary
my_dict.update({"umur": 19, "alamat": "Bandung"})
print(f"Isi dari my_dict setelah diupdate = {my_dict}")


# menghapus item dari dictionary
print(f"\nMenghapus item dari Dictionary")
del my_dict["alamat"]
print(f"Isi dari my_dict setelah dihapus = {my_dict}")
# jika ingin mendapatkan value dari key yang dihapus, bisa menggunakan method pop()
umur = my_dict.pop("umur")
print(f"Isi dari my_dict setelah dihapus = {my_dict},item yang dihapus = {umur}")
# menghapus semuanya menggunakan clear()
my_dict.clear()
print(f"Isi dari my_dict setelah dihapus semua = {my_dict}")


# Looping dictionary
print(f"\nLooping Dictionary")
my_dict = {
    "nama": "Alvin",
    "umur" : "18",
    "alamat" : "Jakarta",
} 

for key in my_dict:
     print(f"key = {key}, value = {my_dict[key]}")

print(my_dict.items())
for key, value in my_dict.items():
    print(f"key = {key}, value = {value}")
    
print(my_dict.keys()) 
print(my_dict.values())
print(f"Banyaknya item di dalam dictionary = {len(my_dict)}")
print(f"Apakah 'nama' ada di dalam dictionary? = {'nama' in my_dict}")
print(f"Apakah Alvin ada di dalam dictionary? = {'Alvin' in my_dict.values()}")



"""  
Latihan soal 1 
- Buatkah sebuah dictionary yang menyimpan informasi tentang sebuah buku, yang memiliki key: judul, penulis, tahun_terbit, dan genre.
- Tampilkan semua informasi tentang buku tersebut menggunakan looping.
- Tambahkan informasi tentang penerbit buku tersebut ke dalam dictionary.
- perbarui tahun terbit buku tersebut.
- Hapus informasi tentang genre buku tersebut.
- Tampilkan semua informasi tentang buku tersebut setelah dilakukan perubahan.
"""
import secrets

# membuat key unik 6 karakter untuk dictionary menggunakan secrets.choice()
key = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(6))

for i in range(5):
    key = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(6))
    print(f"key unik ke-{i+1} = {key}")
    