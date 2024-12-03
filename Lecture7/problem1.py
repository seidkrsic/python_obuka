

""" 
Um, i love, um Python! Um, um i love Coca Cola! Yummy, this is delicious! 
RETURN: 4 
"""

import re 

def main(): 
    text = input("Text: ")
    print(count(text))  

def count(text): 
    # returns number of Um's
    matches = re.findall(r"^[Uu]m[,?!\. ]", text) 
    return len(matches) 

if __name__ == "__main__": 
    main() 
