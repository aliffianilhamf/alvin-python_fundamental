number = 0 

# while (kondisi) : 
    # aksi
    
while (number <= 5):
    print(f"Perulangan ke-{number}")
    
    number = number + 1 #increment
    # number += 1
    

print()
bilangan = 10 
while (bilangan > 0):
    print(f"Perulangan ke-{bilangan}")
    
    bilangan = bilangan - 1 #decrement
    # bilangan -= 1
    
    
print()
state = True
while (state):
    print("Perulangan ke-1")
    
    res = int(input("Masukkan angka (0 untuk berhenti): "))
    
    if (res == 0):
        state = False
        
        
print()
while (True):
    print("Perulangan ke-2")
    
    res = int(input("Masukkan angka (0 untuk berhenti): "))
    
    if (res == 0):
        break
    
    
""""  
Latihan 1 : 
- Buat program untuk menampilkan bilangan genap yang ada dari range 1 - 20 
- output : "{2} adalah bilangan genap


Latihan 2 : 
- User akan menebak angka rahasia
    - angka_rahasia = 10
- lakukan perulangan selama angka yang ditebak user tidak sama dengan angka rahasia
- tebakan user akan diinputkan melalui keyboard menggunakan fungsi input()
- jika tebakan user lebih besar dari angka rahasia, tampilkan "Tebakan anda terlalu besar"
- jika tebakan user lebih kecil dari angka rahasia, tampilkan "Tebakan anda
    terlalu kecil"
- hitung juga berapa kali user menebak angka rahasia 
- kalau tebakan benar, keluar dari perulangan dan tampilkan "Selamat tebakan anda benar" dan tampilkan juga berapa kali user menebak angka rahasia
"Selamat tebakan anda benar, anda menebak sebanyak {jumlah_tebakan} kali"
"""
