nyawa = 100

if (nyawa < 50):
    pass
    
    
print("Nyawa Saat ini : ", nyawa)


# continue
print("\nContoh penggunaan continue")
for i in range(1, 11):
    if (i == 5) : 
        
        continue
    print(f"Perulangan ke-{i}")

print()
i = 0
j = 0
x = 0 
while i < 3:
    x = x + 1
    if x == 1: 
        continue
    print(f"perulangan luar ke-{i}")
    j = 0
    
    while j < 5:
        if (j % 2 == 0):
            j = j + 1
            continue
        print(f"perulangan dalam ke-{j}")
        j = j+ 1
        
    i = j+ 1
    
# loop 1 : i-> 0, x-> 1 --> continue
# loop 2 : i-> 0, x-> 2 --> print perulangan luar ke-0
# loop 3 : i-> 1, x-> 2 --> print perulangan luar ke-1
# loop 4 : i-> 2, x-> 2 --> print perulangan luar ke-2 
    
    
    
    
    
    
    
    
    
print("\nContoh penggunaan break")
for i in range(1, 11):
    if (i == 2) : 
        break
    print(f"Perulangan ke-{i}")

