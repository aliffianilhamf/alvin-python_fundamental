# Game Petualangan Teks Sederhana
# Konsep Pembelajaran: Input/Output, Variabel, Tipe Data, Operator, dan If-Else Statement

print("="*50)
print("  SELAMAT DATANG DI HUTAN MISTERI PYTHON!  ")
print("="*50)
print("Di game ini, keputusanmu sangat menentukan nasibmu.")

# Menerima input nama dari user (Materi: Input & Tipe Data String)
nama = input("Siapa namamu, Petualang berani? ")

print(f"\nSelamat datang, {nama}! Persiapkan dirimu.")

# Inisialisasi Variabel (Materi: Variabel & Tipe Data Integer)
nyawa = 100
skor = 0

print(f"Status Awal: Nyawa = {nyawa} ❤️  | Skor = {skor} ⭐")
print("-"*50)

# --- Skenario 1: Percabangan Dasar ---
print("Kamu berada di persimpangan jalan di tengah hutan gelap.")
print("1. Jalan ke Kiri (Terdengar suara air mengalir)")
print("2. Jalan ke Kanan (Terdengar suara geraman misterius)")

pilihan_1 = input("Jalan mana yang kamu pilih? (1/2): ")

# Materi: If-Elif-Else Statement
if pilihan_1 == '1':
    print("\nKamu menemukan sungai yang jernih. Kamu meminum airnya dan merasa segar.")
    skor += 20  # Operator assignment
elif pilihan_1 == '2':
    print("\nKamu berhadapan dengan Serigala Hutan! Kamu harus bertarung.")
    nyawa -= 45 # Operator assignment
    skor += 50
    print("Kamu berhasil mengalahkannya, tapi kamu terluka.")
else:
    print("\nPilihan tidak valid! Kamu diam kebingungan dan digigit ular berbisa.")
    nyawa -= 20

# Materi: Operator Perbandingan & If Statement untuk peringatan
if nyawa < 30 and nyawa > 0:
    print("\n⚠️ PERINGATAN KRITIS: Nyawamu sudah di bawah 30! Berhati-hatilah di langkah berikutnya!")
elif nyawa <= 0:
    print("\n💀 Kamu kehabisan nyawa terlalu cepat!")

print(f"\n[Status Saat Ini: Nyawa = {nyawa} ❤️  | Skor = {skor} ⭐]")
print("-"*50)

# Cek apakah pemain masih hidup untuk lanjut ke skenario 2
if nyawa > 0:
    # --- Skenario 2: Teka-teki ---
    print("Kamu tiba di depan sebuah gerbang batu kuno.")
    print("Penjaga gerbang muncul dan berkata:")
    print("'Untuk lewat, kamu harus bisa menjawab teka-teki matematika ini:'")
    print("'Berapakah hasil dari (10 * 5) + (20 / 2)?'")
    
    jawaban = input("Masukkan jawabanmu: ")
    
    # Materi: If-Else Statement dengan konversi tipe data (Typecasting)
    if jawaban == "60":
        print("\nPenjaga tersenyum. 'Jawabanmu benar! Silakan masuk dan ambil hartamu.'")
        skor += 100
    else:
        print("\n'SALAH!' teriak penjaga. Dia memukulmu dengan tongkat sihirnya.")
        nyawa -= 80
    
    print(f"\n[Status Saat Ini: Nyawa = {nyawa} ❤️  | Skor = {skor} ⭐]")
    print("-"*50)

# --- Evaluasi Akhir Game ---
print("\n" + "="*50)
if nyawa <= 0:
    print(f"GAME OVER, {nama}! 💀 Kamu gagal bertahan hidup di hutan misteri.")
elif skor >= 100:
    print(f"MENANG SEMPURNA! 🎉 Selamat {nama}, kamu petualang yang sangat hebat!")
else:
    print(f"BERTAHAN HIDUP! 👍 {nama}, kamu berhasil keluar dari hutan meski dengan susah payah.")

print(f"Skor Akhir: {skor} ⭐")
print("="*50)
