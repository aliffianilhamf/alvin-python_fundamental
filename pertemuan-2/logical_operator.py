print("Operator AND")
number_1 = 101

# misal kita ingin membuktikan apakah number_1 itu bilangan ganjil dan positif 
hasil = ((number_1 % 2 == 1) and (number_1 > 0) )
print(f"Hasil dari apakah {number_1} itu bilangan ganjil dan positif = {hasil}")

print("\nOperator OR")
nilai = 88 
persentase_kehadiran = 70

# misal syarat lulus itu nilai lebih dari 90 atu persentase kehadiran lebih dari 75% 
apakah_lulus = ((nilai > 90) or (persentase_kehadiran > 75))
print(f"Hasil dari apakah lulus = {apakah_lulus}")


print("\nOperator NOT")
bawa_sim = "True" 
hasil_not = not bawa_sim # bawa_sim == false
print(f"Hasil dari apakah tidak membawa SIM = {hasil_not}")
if(not bawa_sim):
    # print("Anda tidak membawa sim")
    hasil = "Anda tidak membawa sim"
else: 
    # print("Anda membawa sim")
    hasil = "Anda membawa sim" 
    
    
print(f"Hasil dari apakah membawa SIM = {hasil}")