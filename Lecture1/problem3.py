
""" 
13+24 
4*3
4-2
3/2
"""


def main(): 
    x = input("Expression: ") 
    result = calculate(x) 
    print(f"Solution: {x}={result}") 

def calculate(n): 
    if "+" in n:  
        x, y = n.split("+")  
        x, y = int(x), int(y) 
        return x+y 
    elif "/" in n: 
        x, y = n.split("/") 
        x, y = int(x), int(y) 
        if y == 0:
            return "No solution."
        else: 
            return round(x/y,2)
    elif "-" in n: 
        x, y = n.split("-")
        x, y = int(x), int(y) 
        return x-y 
    elif "*" in n:
        x, y = n.split("*")
        x, y = int(x), int(y) 
        return x*y 


main() 