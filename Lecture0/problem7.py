# ime.prezime@profesor.logate.me 

# Ime Prezime 

# seid.krsic@profesor.logate.me >>> Seid Krsic 
# split("@") 
email = input("Unesi svoj mejl: ") 
x = email.split("@")[0] 
ime, prezime = x.split(".") 
print(ime.title(), prezime.title())  
# x = x.replace(".", " ").title() 
# print(x) 

