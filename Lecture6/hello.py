


# working with Files in Python 


names = [] 
with open("names.txt", "r") as file:  
    for line in file: 
        names.append(line.strip()) 

for name in sorted(names): 
    print(f"hello, {name}") 

