class Mobil: 
    # Konstruktor adalah method yang akan dieksekusi pertama kali ketika sebuah object dibuat dari sebuah kelas
    def __init__(self, merk="", tipe=""):
        # print("Konstruktor dijalankan")
        # Data / Atribut
        self.merk = merk
        self.tipe = tipe
        self.kecepatan = 0
    
    
    
    def nyalakan_mesin(self):
        print(f"Brummm! Mesin {self.merk} {self.tipe} dinyalakan")
    
    def tambah_kecepatan(self, kecepatan):
        self.kecepatan += kecepatan
        print(f"Kecepatan {self.merk} {self.tipe} bertambah menjadi {self.kecepatan} km/jam")        
        
# inheritance 
#  kita akan membuat kelas MobilListrik yang merupakan turunan dari kelas Mobil. tapi dia punya fitur khusus yang tidak dimiliki mobil biasa.
# yakni baterai dan kemampuasn untuk mengisi daya baterai.
class MobilListrik(Mobil):
    def __init__(self, merk="", tipe="", kapasitas_baterai=0):
        super().__init__(merk, tipe)
        
        # fitur eksklusif mobil listrik 
        self.kapasitas_baterai = kapasitas_baterai
        
    def isi_daya(self, daya):
        print(f"Mobil {self.merk} {self.tipe} sedang mengisi daya sebesar {daya} kWh")
        
        

# test 
print(f"Test Mobil Biasa")
mobil_keluarga = Mobil("Toyota", "Avanza")
mobil_keluarga.nyalakan_mesin()
mobil_keluarga.tambah_kecepatan(20) 

print("\nTest Mobil Listrik")
chery = MobilListrik("Chery", "Tiggo 8 CSH", 70)
chery.nyalakan_mesin()  
chery.tambah_kecepatan(50) # warisan dari parent class Mobil
chery.isi_daya(20) # fitur khusus dari child (inheritance) class MobilListrik

        