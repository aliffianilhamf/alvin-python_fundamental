nyawa = 0 


def tambah_nyawa():
    global nyawa 
    nyawa += 1
    print(f"Nyawa bertambah menjadi {nyawa}")


if __name__ == "__main__":
    print(f"Nyawa awal = {nyawa}")
    tambah_nyawa()
    print(f"Nyawa setelah ditambah = {nyawa}")