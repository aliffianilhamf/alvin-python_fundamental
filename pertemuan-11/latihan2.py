# membuat class RekeningBank yang bisa menyimpan data nasabah dan melakukan transaksi dasar secara independen

# 1. Buat Class rekening bank yang memiliki konstruktor dan memiliki atribut nama, dan saldo
# 2. Buat method untuk menampilkan saldo yang hanya bertugas melakukan print nama dan saldo saat ini. 
# 3. Buat method untuk melakukan setoran yang menerima parameter jumlah setoran, lalu menambahkan jumlah setoran ke saldo saat ini lalu print pesan sukses beserta jumlah saldo terbaru
# 4. Buat method untuk melakukan penarikan yang menerima parameter jumlah penarikan, lalu mengurangi jumlah penarikan dari saldo saat ini. Jika saldo tidak cukup, maka print pesan gagal beserta jumlah saldo saat ini. Jika berhasil, print pesan sukses beserta jumlah saldo terbaru

# test programnya dengan membuat 2 object rekening bank yang berbeda, lalu lakukan transaksi setoran dan penarikan pada masing-masing object rekening bank tersebut.


# inheritance 
#  membuat class Rekening bisnis yang memiliki atribut baru berupa "nama perusahaan"   dan memiliki method baru berupa ajukan pinjaman yang menerima parameter jumlah pinjaman, lalu print pesan sukses beserta jumlah pinjaman yang diajukan.

# polymorphism 
# membuat class rekening kredit yang memiliki atribut baru berupa "limit kredit" dan memiliki method yang sama dengan class rekening bank yaitu penarikan, namun dengan aturan baru yaitu jika penarikan melebihi limit kredit maka print pesan gagal beserta jumlah limit kredit saat ini. Jika berhasil, print pesan sukses beserta jumlah limit kredit terbaru. jadi class rekening kredit ini method penarikan akan menimpa method penarikan yang ada di class rekening bank. 


# test programnya dengan membuat 1 object rekening bisnis dan 1 object rekening kredit, lalu lakukan transaksi setoran dan penarikan pada masing-masing object rekening tersebut. dan harusnya saldo bisa minus pada rekening kredit jika penarikan melebihi saldo saat ini, namun tidak boleh melebihi limit kredit.