def sapa(**kwargs):
    # print(kwargs)
    # print(kwargs["nama"])
    # print(kwargs["umur"])
    for k, v in kwargs.items():
        print(f"{k} = {v}")
    
    
sapa(nama="Alvin", umur=18, alamat="Jakarta")
sapa(nama="Budi", umur=20, alamat="Bandung", hobi="Membaca")
sapa(nama="Caca", umur=22, alamat="Semarang", hobi="Menulis", pekerjaan="Programmer")