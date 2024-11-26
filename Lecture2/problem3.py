

# omoguci korisniku da unese 4 broja: 
# 1, 10, 2, 52
# prosjecna temperatura 
# broj gradova cija je temperatura bila ispod prosjeka 

count = 0
temperatures = [] 
x = int(input("Unesi koliko gradova ti treba: "))
for i in range(x): 
    n = int(input("Unesi temperaturu: ")) 
    temperatures.append(n) 

average = sum(temperatures) / len(temperatures) 

for temperature in temperatures: 
    if temperature < average: 
        count += 1 
print(f"Broj gradova cija je temperatura ispod prosjecne je: {count}") 