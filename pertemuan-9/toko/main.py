import os 
from operasional.storage.data import load_data, save_data
from operasional.layanan.kasir import proses_transaksi
from operasional.util.cetak import cetak_nota


#             toko/       data    / produk.json --> toko/data/produk.json   
PATH_PRODUK = os.path.join(os.path.curdir,"pertemuan-9","toko","data", "produk.json")
PATH_TRANSAKSI = os.path.join(os.path.curdir,"pertemuan-9","toko", "data", "transaksi.json")

def prepare_data():
    if not os.path.exists(PATH_PRODUK):
        produk_awal = [
            {"kode" : "p01", "nama" : "Indomie Goreng", "harga" : 3000, "stok" : 10},
            {"kode" : "p02", "nama" : "Indomie Rebus", "harga" : 3000, "stok" : 10},
            {"kode" : "p03", "nama" : "Indomie Soto", "harga" : 3000, "stok" : 10},
            {"kode" : "p04", "nama" : "Indomie Kari Ayam", "harga" : 3000, "stok" : 10},
            {"kode" : "p05", "nama" : "Indomie Ayam Bawang", "harga" : 3000, "stok" : 10}
        ]
        
        save_data(PATH_PRODUK, produk_awal)
        
def main():
    prepare_data() 
    produk_list = load_data(PATH_PRODUK)
    transaksi_list = load_data(PATH_TRANSAKSI)
    
    # menampilkan daftar produk 
    print("Daftar Produk")
    print(f"{'Kode':<5}  {'Nama':^20}  {'Harga':<10}  {'Stok':<5}")
    for item in produk_list:
        print(f"{item['kode']:<5}  {item['nama']:<20}  {item['harga']:<10}  {item['stok']:<5}")
    print("=" * 50)
    
    
    kode = input("Masukkan Kode Barang: ").strip()
    quantity = input("Masukkan Jumlah Barang: ").strip()
    
    if not quantity.isdigit():
        print("Jumlah harus berupa angka")
        return
    
    status, pesan , pesanan =  proses_transaksi(produk_list, kode, int(quantity))
    
    if status and pesanan:
        save_data(PATH_PRODUK, produk_list)
        
        # menyimpan data transaksi
        transaksi_list.append(pesanan)
        save_data(PATH_TRANSAKSI, transaksi_list) 
        
        cetak_nota(pesanan)
        print(pesan)
    
if __name__ == "__main__":
    main()