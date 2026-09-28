print("Nested loop untuk while")
i = 0
j = 0
while i < 3:
    print(f"perulangan luar ke-{i}")
    j = 0
    while j < 5:
        print(f"perulangan dalam ke-{j}")
        j += 1
    i += 1
    
    
print("\nNested loop untuk for")
for i in range(3):
    print(f"perulangan luar ke-{i}")
    for j in range(5):
        print(f"perulangan dalam ke-{j}")
    