


# ipisati brojeve od 1 do 10 jedan pored drugog, koristeci while petlju 
# 1 2 3 4 ... 10 

# i = 1 
# while i<=10: 
#     print(i, end=" ") 
#     i += 1 


# napravite program koji ispisuje brojeve od 50 do 100, svaki drugi broj. 
# 50 52 54 ... 100 

# i = 50 
# while i<=100: 
#     print(i, end=" ") 
#     i+= 2 

# napravite program koji ispisuje brojeve od 50 do 101, svaki drugi broj. 
# 50 52 54 ... 100 101 

i = 50 
while i<=101: 
    if i % 2 == 0: 
        print(i, end=" ") 
    i+=2 
    
print(101) 