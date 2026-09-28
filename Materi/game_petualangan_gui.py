import tkinter as tk
from tkinter import messagebox

# ==========================================
# Variabel State Game (Menyimpan data)
# ==========================================
nyawa = 100
skor = 0
nama = ""

def mulai_game():
    global nama
    nama = entry_input.get()
    
    # Mengecek apakah input nama kosong
    if nama == "":
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        return
    
    # Update tampilan GUI
    label_status.config(text=f"Status: Nyawa = {nyawa} ❤️ | Skor = {skor} ⭐")
    label_cerita.config(text=f"Selamat datang, {nama}!\n\nKamu berada di persimpangan jalan di tengah hutan gelap.\n1. Jalan ke Kiri (Terdengar suara air mengalir)\n2. Jalan ke Kanan (Terdengar suara geraman misterius)")
    
    entry_input.delete(0, tk.END)
    btn_submit.config(text="Pilih (1 atau 2)", command=proses_pilihan)

def proses_pilihan():
    global nyawa, skor
    pilihan = entry_input.get()
    
    # ---------------------------------------------
    # Materi: If-Elif-Else Statement & Operator
    # ---------------------------------------------
    if pilihan == '1':
        cerita = "Kamu menemukan sungai jernih. Kamu meminum airnya dan merasa segar."
        skor += 20
    elif pilihan == '2':
        cerita = "Kamu berhadapan dengan Serigala Hutan! Kamu berhasil menang, tapi terluka."
        nyawa -= 45
        skor += 50
    else:
        cerita = "Pilihan tidak valid! Kamu kebingungan dan digigit ular berbisa."
        nyawa -= 20
        
    peringatan = ""
    # Materi: Operator Perbandingan dan Logika
    if nyawa < 30 and nyawa > 0:
        peringatan = "\n\n⚠️ PERINGATAN KRITIS: Nyawamu di bawah 30! Hati-hati!"
    
    # Update Status Nyawa & Skor di layar
    label_status.config(text=f"Status: Nyawa = {nyawa} ❤️ | Skor = {skor} ⭐")
    
    if nyawa <= 0:
        label_cerita.config(text=cerita + "\n\n💀 Kamu kehabisan nyawa terlalu cepat! GAME OVER.")
        entry_input.config(state=tk.DISABLED)
        btn_submit.config(state=tk.DISABLED)
    else:
        label_cerita.config(text=cerita + peringatan + "\n\nSelanjutnya, penjaga gerbang batu muncul dan berkata:\n'Berapakah hasil dari (10 * 5) + (20 / 2)?'")
        entry_input.delete(0, tk.END)
        btn_submit.config(text="Jawab", command=proses_teka_teki)

def proses_teka_teki():
    global nyawa, skor
    jawaban = entry_input.get()
    
    # ---------------------------------------------
    # Materi: If-Else Statement 
    # ---------------------------------------------
    if jawaban == "60":
        cerita = "Penjaga tersenyum. 'Jawabanmu benar! Silakan masuk.'"
        skor += 100
    else:
        cerita = "'SALAH!' teriak penjaga. Dia memukulmu."
        nyawa -= 80
        
    label_status.config(text=f"Status: Nyawa = {nyawa} ❤️ | Skor = {skor} ⭐")
    
    # Evaluasi Akhir Game
    if nyawa <= 0:
        akhir = "\n\n💀 GAME OVER! Kamu gagal bertahan hidup."
    elif skor >= 100:
        akhir = f"\n\n🎉 MENANG SEMPURNA! {nama}, kamu petualang yang hebat!"
    else:
        akhir = f"\n\n👍 BERTAHAN HIDUP! {nama}, kamu berhasil keluar dari hutan."
        
    label_cerita.config(text=cerita + akhir)
    entry_input.config(state=tk.DISABLED)
    btn_submit.config(state=tk.DISABLED)

# ==========================================
# SETUP JENDELA GUI (Menggunakan Tkinter)
# ==========================================
root = tk.Tk()
root.title("Game Petualangan Hutan Misteri (GUI)")
root.geometry("500x450")
root.config(bg="#2c3e50")

# Styling Font
font_title = ("Helvetica", 16, "bold")
font_text = ("Helvetica", 12)

# Elemen-elemen GUI (Widget)
label_judul = tk.Label(root, text="🌳 HUTAN MISTERI PYTHON 🌳", font=font_title, bg="#2c3e50", fg="white")
label_judul.pack(pady=15)

label_status = tk.Label(root, text="Status: Nyawa = 100 ❤️ | Skor = 0 ⭐", font=font_text, bg="#2c3e50", fg="#f1c40f")
label_status.pack(pady=5)

label_cerita = tk.Label(root, text="Di game ini, keputusanmu sangat menentukan nasibmu.\n\nSiapa namamu, Petualang?", font=font_text, bg="#2c3e50", fg="white", justify=tk.CENTER, wraplength=450)
label_cerita.pack(pady=20)

entry_input = tk.Entry(root, font=font_text, width=30, justify=tk.CENTER)
entry_input.pack(pady=10)

btn_submit = tk.Button(root, text="Mulai", font=("Helvetica", 12, "bold"), command=mulai_game, bg="#3498db", fg="white", padx=20, pady=5)
btn_submit.pack(pady=15)

# Menjalankan aplikasi
root.mainloop()
