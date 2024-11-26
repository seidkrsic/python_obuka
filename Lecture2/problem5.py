

# add_dots >>> python -> p.y.t.h.o.n. 
# "" + "p." > "p." + "y." > "p.y." 

def add_dots(string): 
    x = "" 
    for letter in string: 
        x += letter + "." 
    
    return x 

result = add_dots("python") 
print(result)  # >>> p.y.t.h.o.n.