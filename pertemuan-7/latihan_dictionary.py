import datetime as dt
import secrets

template_mhs = {
    "nama" : "Alvin",
    "nim" : "123456789",
    "sks_lulus" : 100,
    "beasiswa"  : True, 
    "lahir" : dt.datetime(2000, 1, 1)
}

# template_mhs2 = template_mhs

# print(f"template_mhs = {template_mhs}")
# print(f"template_mhs2 = {template_mhs2}")

# template_mhs2["nama"] = "Budi"
# print(f"\ntemplate_mhs = {template_mhs}")
# print(f"template_mhs2 = {template_mhs2}")

# template_mhs3 = template_mhs.copy()
# print(f"\ntemplate_mhs = {template_mhs}")
# print(f"template_mhs2 = {template_mhs2}")
# print(f"template_mhs3 = {template_mhs3}")

# template_mhs3["nama"] = "Caca"
# print("\nupdate template_mhs3['nama'] menjadi 'Caca'")
# print(f"template_mhs = {template_mhs}")
# print(f"template_mhs2 = {template_mhs2}")
# print(f"template_mhs3 = {template_mhs3}")

# print("\nupdate template_mhs['nama'] menjadi 'Dodi'")
# template_mhs["nama"] = "Dodi"
# print(f"template_mhs = {template_mhs}")
# print(f"template_mhs2 = {template_mhs2}")
# print(f"template_mhs3 = {template_mhs3}")
data_mhs = {}

while True: 
    # mhs  = dict.fromkeys(template_mhs.keys())
    template_mhs["nama"] = input("Masukkan nama mahasiswa: ")
    template_mhs["nim"] = input("Masukkan NIM mahasiswa: ")
    template_mhs["sks_lulus"] = int(input("Masukkan jumlah SKS lulus mahasiswa: "))
    template_mhs["beasiswa"] = input("Apakah mahasiswa mendapatkan beasiswa? (y/n): ").lower() == "y"
    tahun = int(input("Masukkan tahun lahir mahasiswa: "))
    bulan = int(input("Masukkan bulan lahir mahasiswa: "))
    hari = int(input("Masukkan hari lahir mahasiswa: "))
    template_mhs["lahir"] = dt.datetime(tahun, bulan, hari)
    
    key = "".join((secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(6)))
    data_mhs.update({key: template_mhs.copy()})
    
    print(f"{'KEY':<6} {'NAMA':<20} {'NIM':<10} {'SKS LULUS':<10} {'BEASISWA':<10} {'LAHIR':<10}")
    print("-"*70)
    for key in data_mhs:
        print(f"{key:<6} {data_mhs[key]['nama']:<20} {data_mhs[key]['nim']:<10} {data_mhs[key]['sks_lulus']:<10} {data_mhs[key]['beasiswa']:<10} {data_mhs[key]['lahir'].strftime('%Y-%m-%d'):<10}")
        
    # for key, value in data_mhs.items():
    #     print(f"KEY = {key}, NAMA = {value['nama']}, NIM = {value['nim']}, SKS LULUS = {value['sks_lulus']}, BEASISWA = {value['beasiswa']}, LAHIR = {value['lahir'].strftime('%Y-%m-%d')}")
        
        
    lanjut = input("Apakah ingin menambahkan data mahasiswa lagi? (y/n): ").lower()
    if lanjut != "y":
        break
    
print("Terima kasih telah menggunakan program ini.")