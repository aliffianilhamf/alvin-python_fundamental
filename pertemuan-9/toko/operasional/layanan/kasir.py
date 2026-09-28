import datetime


def cari_produk(daftar_produk, kode):
    for produk in daftar_produk:
        if (produk['kode'].lower() == kode.lower()):
            return produk
        
    return None


def proses_transaksi(daftar_produk, kode, jumlah):
    produk = cari_produk(daftar_produk, kode)
    
    if not produk:
        return False, "Produk tidak ditemukan"
    
    if jumlah <= 0:
        return False, "Jumlah harus lebih dari 0" 
    
    if produk['stok'] < jumlah : 
        return False, f"Stok tidak cukup, stock tersedia: {produk['stok']}"
    
    # kurangi stok barang 
    produk["stok"] -= jumlah 
    subtotal = produk['harga'] * jumlah 
    
    data = {
        "tanggal" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "kode" : produk["kode"],
        "nama" : produk["nama"],
        "harga" : produk["harga"],
        "jumlah" : jumlah,
        "subtotal" : subtotal
    }
    
    return True, "Transaksi berhaasil diproses", data