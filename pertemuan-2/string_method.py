# Memanipulasi huruf
print("Memanipulasi huruf")
text = "Belajar PYthon FUNdamental"
print(f"Original        : {text}")
print(f"Lowercase       : {text.lower()}")
print(f"Uppercase       : {text.upper()}")
print(f"Capitalize      : {text.capitalize()}")
print(f"Title           : {text.title()}")
print(f"Swapcase        : {text.swapcase()}")

print("\nPembersihan spasi")
data_kotor = "   Data ini kotor   "
print(f"Original        : '{data_kotor}'")
data_bersih = data_kotor.strip()
print(f"Strip           : '{data_bersih}'")
data_bersih = data_kotor.lstrip()
print(f"Lstrip          : '{data_bersih}'")
data_bersih = data_kotor.rstrip()
print(f"Rstrip          : '{data_bersih}'")

print(f"Splitting (memisah string)")
judul = "Pangeran dari kota selatan"
judul_split = judul.split(" ")
print(f"Original        : '{judul}'")
print(f"Split           : {judul_split}")

kode_barang = "KSM-001-2023"
kode_barang_split = kode_barang.split("-")
print(f"Original        : '{kode_barang}'")
print(f"Split           : {kode_barang_split}")
print(f"kode KSM        : {kode_barang_split[0]}   ")

print("\nPengecekan tipe konten")
string_1 = "3"
# ,mengecek apakah string_1 hanya terdiri dari huruf
print(f"Apakah {string_1} hanya terdiri dari huruf? {string_1.isalpha()}")
# mengecek angka 
print(f"Apakah {string_1} hanya terdiri dari angka? {string_1.isdigit()}")
# mengecek keduanya 
print(f"Apakah {string_1} hanya terdiri dari huruf dan angka? {string_1.isalnum()}")

print("\nMengubah / replace data strong")
kode_barang = "KSM-001-2023"
kode_barang_replace = kode_barang.replace("KSM", "KTM").replace("001", "002")
print(f"Original        : '{kode_barang}'")
print(f"Replace         : '{kode_barang_replace}'")

"""  
latihan Soal 1 
Bersihkan spasi diawal / akhir dan ubah menjadi huruf kecil semua
- input : "   Belajar PYthon FUNdamental   "
- output : "belajar python fundamental"


latihan soal 2 
hapus "Rp" (termasuk spasi setelah Rp) dan hapus tanda titik(.)
input = "Rp 1.000.000"
output = "1000000"


latihan 3 
Pecah string berdasarkan karakter (-)
-input : "IPHONE13-PRO-MAX-256GB"
-output : ['IPHONE13', 'PRO', 'MAX', '256GB']

latihan soal 4
gabungkan list menggunakan separator (-)
- input : ['IPHONE13', 'PRO', 'MAX', '256GB']
- output : "IPHONE13-PRO-MAX-256GB"

latihan soal 5 
Pisahkan string berdasarkan |, dan bersihkan spasi diawal / akhir setiap item, lalu ubah jadi huruf kecil semua, ubah spasi di tengah menjadi underscore (_), hapus tanda baca kurung buka 
- input : "   Nama Customer | Total Belanja (IDR) | Alamat Pengiriman    "
- output : ["nama_customer_", "total_belanja_idr_", "_alamat_pengiriman"]
"""

# format specifier 
nilai_pi = 3.14159265358979323846 

# mengatur jumlah angka dibelakang koma 
print(f"Nilai PIU (2 desimal) : {nilai_pi:.2f}")
print(f"Nilai PIU (4 desimal) : {nilai_pi:.4f}")

# format rupiah 
harga = 1250000 # Rp 1,250,000.00
print(f"Harga : Rp {harga:,.2f}")  # koma digunakanuntuk memisahkan ribuan