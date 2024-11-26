

""" 
Napraviti program u kojem cete kreirati funkciju 
broj_cipela -- > ima tri argumenta 

broj_cipela(3,4,3) ---> 3*4 + 4*2 + 3*4 = ... 

korisnik unosi broj macaka, kokosaka i lavova. 

"""

def broj_cipela(macke,kokoske,lavovi):
    return macke*4 + kokoske*2 + lavovi*4 

x = int(input("Unesi broj macaka: "))
y = int(input("Unesi broj kokosaka: "))
z = int(input("Unesi broj lavova: ")) #"5"  -- > 5  

result = broj_cipela(x,y,z)  
print(result) 

