# Range adalah sebuah fungsi bawaan Python yang digunakan untuk menghasilkan urutan angka. Fungsi ini sering digunakan dalam perulangan (loop) untuk mengulang blok kode tertentu sejumlah kali.
# --- start -. defaultnya 0
# --- stop  - akan berhenti sebelum value stopnya
# --- step

# range(start, stop, step)
# range(start, stop) -> step defaultnya 1
# range(stop) -> start defaultnya 0, step defaultnya 1


for i in range(0, 10, 2):
    print(f"Perulangan ke-{i}")


print("Ini line 1")
print("Ini line 2")

print(f"\nFor loop untuk string")
judul = "Belajar Python" 

for char in judul : 
    if char.lower() in 'aiueo':
        # print("Bingo!!")
        print(char)
        
        
print(f"\nFor loop untuk list")
numbers = [1, 2, 3, 4, 5]
max = 1
for number in numbers : 
    if number > max:
        max = number
    print(f"Isi dari list : {number}")
    
    
"""    
latihan 1 : 
- kalimat = "Dokumen ini berisi materi python"
- print hanya huruf konsonan dari kalimat diatas menggunakan for loop dan juga print berapa huruf konsonan yang ada di kalimat tersebut


Latihan 2 :
-numbers = [ 30, 40, 33, 56, 78, 90, 100, 120]
- cari nilai maksimum dan minimum dari list numbers diatas menggunakan for loop
- tidak boleh menggunakan fungsi bawaan max() dan min()
- print hasilnya dengan format : "Nilai maksimum dari list numbers adalah {nilai_maksimum}" dan "Nilai minimum dari list numbers adalah {nilai_minimum}" di luar for loop

Latihan 3 : 
- numbers = [21, 34, 43, 22, 44, 55, 66, 77, 88, 99]
- hitung total dari nilai genap dan ganjil dari list numbers diatas menggunakan for loop


"""
total_genap=0
total_ganjil=0

for i in numbers:
    if (i % 2 == 1):
        total_ganjil += i
    elif (i % 2 == 0):
        total_genap += i
    
    
print(f"Total nilai genap dari list numbers adalah {total_genap}")
print(f"Total nilai ganjil dari list numbers adalah {total_ganjil}")