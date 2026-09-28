def calculate(*args):
    # print(args) 
    # print(args[0])
    # print(args[1])
    result = 0
    for item in args:
        result += item
        
    print(f"Hasil penjumlahan dari {args} = {result}")
    
calculate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

"""" 
Latihan soal 1
- Buatlah fungsi yang menerima *args, lalu kembalikan hasil perkalian dari semua argumen yang diterima

Latohan soal 2
- Buat fungsi yang menerima 2 paramater: 
1. nama_toko (string)
2. *args (list of string)
- Fungsi akan menampilkan nama toko, lalu menampilkan semua item yang diterima dari *args
"""