

# omogucite korisniku da unosi neki broj 
# ako je taj broj < 0, raise ValuError sa porukom... 
# odredite kvadratni korijen unijetog 

# import math 

# print(math.sqrt(4))

import math 

try: 
    x = int(input("Unesi broj: ")) 
    if x < 0: 
        raise ValueError("Ne moze se izracunati korijen iz negativnog broja.") 
    result = math.sqrt(x) 
    print(round(result))  
except ValueError as error: 
    print(f"Greska: {error}") 