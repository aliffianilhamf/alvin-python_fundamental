# Sistem perpustakaan sederhana 

# Kelas Buku memiliki atribut judul dan status, status memiliki default nilai "tersedia" 

# Kelas Perpustakaan memiliki method tambah_buku, cari_buku, pinjam_buku, dan kembalikan_buku. 
    # tambah_buku akan menambahkan buku kedalam daftar buku perpustakaan, lalu print "Buku [judul] berhasil ditambahkan ke perpustakaan"
    
    # cari_buku akan mencari buku berdasarkan judul pada daftar buku perpustakaan, jika ditemukan return buku tersebut, jika tidak return None
    
    # pinjam_buku akan memanggil method cari_buku, jika buku ditemukan dan status buku adalah "tersedia", maka ubah status buku menjadi "dipinjam" dan print "Buku [judul] berhasil dipinjam", jika status buku adalah "dipinjam" maka print "Buku [judul] sedang dipinjam", jika buku tidak ditemukan maka print "Buku [judul] tidak ditemukan"
    
    # kembalikan_buku akan memanggil method cari_buku, jika buku ditemukan dan status buku adalah "dipinjam", maka ubah status buku menjadi "tersedia" dan print "Buku [judul] berhasil dikembalikan", jika status buku adalah "tersedia" maka print "Buku [judul] belum dipinjam", jika buku tidak ditemukan maka print "Buku [judul] tidak ditemukan"
    
    
# Contoh Alur kerja program 
# 1. Buat object perpustakaan dari kelas Perpustakaan
# 2. Tambahkan buku ke perpustakaan menggunakan method tambah_buku
# 3. Pinjam buku menggunakan method pinjam_buku
# 4. Kembalikan buku menggunakan method kembalikan_buku