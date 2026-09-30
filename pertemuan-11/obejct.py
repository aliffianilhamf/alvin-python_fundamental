class Mobil: 
    # Konstruktor adalah method yang akan dieksekusi pertama kali ketika sebuah object dibuat dari sebuah kelas
    def __init__(self, merk="", warna=""):
        print("Konstruktor dijalankan")
        # Data / Atribut
        self.merk = merk
        self.warna = warna
    
    
    
    # Perilaku / Method
    def maju(self, merk):
        print("Mobil maju")
        print(f"dari dalam class:{merk}. dari parameter:{merk}")
        
    def mundur(self):
        print("Mobil mundur")
        
        
# object mobil1 dibuat dari kelas Mobil
# mobil1 = Mobil() # Membuat object dari kelas Mobil

# print(mobil1.merk) 
# print(mobil1.warna) 
# mobil1.maju("Pajero")
# mobil1.mundur()

mobil_avanza = Mobil() # Membuat object dari kelas Mobil
mobil_avanza.merk = "Toyota"
print(mobil_avanza.merk) 

mobil_avanza.warna = "Putih"
print(mobil_avanza.warna)

print("=====================================")

mobil_crv = Mobil() # Membuat object dari kelas Mobil
mobil_crv.merk = "Honda"
print(mobil_crv.merk)

mobil_crv.warna = "Hitam"
print(mobil_crv.warna)

print("=====================================")

mobil_fronx = Mobil("Suzuki", "Blue")
print(mobil_fronx.merk)
print(mobil_fronx.warna)