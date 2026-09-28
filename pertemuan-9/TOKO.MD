# Struktur direcktori proyek

```text
toko/
├── data/
│   ├── produk.json          # Database barang & stok
│   └── transaksi.json       # Rekap nota transaksi
├── operasional/
│   ├── storage/
│   │   └── database.py      # Operasi baca/tulis JSON + os
│   ├── layanan/
│   │   └── kasir.py         # Logika hitung belanja & potong stok
│   └── utilitas/
│       └── cetak.py         # Format mata uang & struk belanja
└── main.py                  # Antarmuka CLI utama
```

# Implementasi kode

## Penyimpanan data : `operasional/storage/database.py`

- Fungsi `load_data(path)` : Membaca file JSON dari path yang diberikan dan mengembalikan data sebagai objek Python. Jika file tidak ditemukan, mengembalikan list kosong.
- Fungsi `save_data(path, data)` : Menyimpan data ke file JSON di path yang diberikan. Jika folder tidak ada, membuat folder tersebut terlebih dahulu.
- menggunakan modul `os` untuk operasi file dan folder, serta modul `json` untuk serialisasi dan deserialisasi data JSON.

## Logika kasir : `operasional/layanan/kasir.py`

- Fungsi `cari_produk(kode)` : Mencari produk berdasarkan kode dari database produk. Mengembalikan objek produk jika ditemukan, atau None jika tidak ditemukan.
- Fungsi `proses_transaksi(kode, jumlah)` : Memproses transaksi pembelian dengan kode produk dan jumlah yang diberikan. Mengurangi stok produk, menghitung subtotal, dan menyimpan transaksi ke database transaksi. Mengembalikan objek transaksi jika berhasil, atau None jika gagal (misalnya stok tidak cukup).

## Utilitas cetak : `operasional/utilitas/cetak.py`

- Fungsi `cetak_nota(pesanan)` : Mencetak struk pembelian dengan format yang rapi, menampilkan nama barang, harga, jumlah, dan subtotal.

## Main entry point : `main.py`

- Definisikan Path produk dan transaksi.
- membuat data awal produk jika file produk.json tidak ada. yang dimasukkan ke sebuah fungsi lalu memanggil `save_data` untuk menyimpan data awal ke file produk.json.
- buat fungsi `main()` untuk menjalankan antarmuka CLI utama, yang memungkinkan pengguna untuk memasukkan kode produk dan jumlah pembelian, memproses transaksi, dan mencetak struk pembelian.
