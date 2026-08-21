""" 
Typecasting adalah proses mengubah tipe data dari satu tipe ke tipe data lain. Di Python, kita dapat melakukan typecasting menggunakan fungsi bawaan seperti int(), float(), str(), dll.
"""

print("konversi dari string ke int")
nama = "Aliffian"
# nama_int = int(nama)

number_str = "100"
print(f"{number_str} (tipe data sebelum di konversi: {type(number_str)})")
number_int = int(number_str)
print(f"{number_int} (tipe data setelah di konversi: {type(number_int)})")

print("\nkonversi dari string ke float")
number_str = "3.14"
print(f"{number_str} (tipe data sebelum di konversi: {type(number_str)})")
number_float = float(number_str)
print(f"{number_float} (tipe data setelah di konversi: {type(number_float)})")

print("\nkonversi string ke boolean")
bool_str = ""
print(f"{bool_str} (tipe data sebelum di konversi: {type(bool_str)})")
bool_bool = bool(bool_str)
print(f"{bool_bool} (tipe data setelah di konversi: {type(bool_bool)})")


print("\nkonversi dari int ke float")
number_int = 10
print(f"{number_int} (tipe data sebelum di konversi: {type(number_int)})")
number_float = float(number_int)
print(f"{number_float} (tipe data setelah di konversi: {type(number_float)})")


print("\nkonversi dari float ke int")
number_float = 3.14
print(f"{number_float} (tipe data sebelum di konversi: {type(number_float)})")
number_int = int(number_float)
print(f"{number_int} (tipe data setelah di konversi: {type(number_int)})")

