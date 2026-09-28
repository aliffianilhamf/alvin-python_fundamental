# Set adalah tipe data yang menyimpan nilai unik, dan tidak memiliki urutan
# set juga tidak dapat diakses menggunakan index, karena tidak memiliki urutan 

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(f"Isi dari my_set = {my_set}")

# print(my_set[0]) # akan error karena set tidak memiliki index
for item in my_set:
    print(f"Isi dari item = {item}")
    
print(f"\nMenambahkan item ke dalam set")
# menambahkan item ke dalam set menggunakan add()
my_set.add(10)
print(f"Isi dari my_set setelah ditambahkan = {my_set}")

# menghapus item dari set menggunakan remove()
print(f"\nMenghapus item dari set")
my_set.remove(5)
print(f"Isi dari my_set setelah dihapus = {my_set}")