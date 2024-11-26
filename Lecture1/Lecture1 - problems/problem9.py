


# korisnik unosi neki broj 

# ako je unio paran broj --- 20 >>> 21 
# ako je unio neparan broj -- 21 >>> 23 

number = int(input("Unesi neki broj: ")) 
if number % 2 != 0: 
    print(number + 2) 
else: 
    print(number + 1)  

