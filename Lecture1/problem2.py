

""" 
isinstance u pythonu 
w3schools -->  
"""

def main(): 
    x = input("Input: ") 
    x = int(x) 
    if is_integer(x): 
        print(True) 
    else: 
        print(False) 

def is_integer(n):
    return isinstance(n,int)  # True/False 

main() 