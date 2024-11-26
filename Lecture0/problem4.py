

# napraviti tri promjenljive u koje se cuva unos korisnika 
# ime takodje unosi 

# pizza, hambureger i burek. 

""" 
Marko voli sljedecu hranu: 
- Pizza 
- Hamburger
- Burek 
"""

hrana1 = input("Unesi omiljenu hranu: ")
hrana2 = input("Unesi omiljenu hranu: ") 
hrana3 = input("Unesi omiljenu hranu: ") 

hrana1 = hrana1.title() 
hrana2 = hrana2.title()
hrana3 = hrana3.title() 

ime = input("Unesi svoje ime: ") 

print(f"{ime.title()} voli sljedecu hranu: ") 
print(f"- {hrana1}\n- {hrana2}\n- {hrana3}")  
