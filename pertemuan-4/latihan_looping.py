# tabel perkalian 1-5
for i in range(1, 6):
    for j in range(1, 6): 
        print(i * j, end="\t")
    print()   
    
    
# pola 1
print()
n_segitiga = 5
for i in range(1, n_segitiga + 1):
   print("*" * i)
   
#    pola 2
print()
for i in range(n_segitiga, 0, -1):
    print("*" * i)
 
   
print()
for i in range(1, n_segitiga + 1):
    spasi =  n_segitiga - i
    print(f"{' ' * spasi}{'*' * i}")
    
print()
jumlah_baris = 5
for i in range(1, jumlah_baris + 1):
    spasi = jumlah_baris - i
    print(f"{' ' * spasi}{'*' * (2 * i - 1)}")