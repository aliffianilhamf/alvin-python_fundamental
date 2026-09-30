class Mobil: 
    # Konstruktor adalah method yang akan dieksekusi pertama kali ketika sebuah object dibuat dari sebuah kelas
    def __init__(self):
        print("Konstruktor dijalankan")
    
    # Data / Atribut
    merk = "Mitsubishi"
    warna = "Hitam"
    
    # Perilaku / Method
    def maju(self, merk):
        print("Mobil maju")
        print(f"{self.merk} {merk}")
        
    def mundur(self):
        print("Mobil mundur")
        
        
mobil1 = Mobil() # Membuat object dari kelas Mobil
    