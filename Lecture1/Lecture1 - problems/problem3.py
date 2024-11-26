

# napraviti funkciju 
# sgn(x) >>> x<0 -> -1, x>0 -> 1, x==0 -> 0 

def sgn(x): 
    if x < 0: 
        return -1 
    elif x > 0: 
        return 1 
    else: 
        return 0  

print(sgn(-10))  