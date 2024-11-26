

""" 
startswith ... metod u pythonu 
Unesi neki pozdrav 
Heeey >>> $20 
Hello >>> $0 
What's up? $100 
"""

def bank_greeting(): 
    greeting = input("Enter your greeting: ") 
    if greeting.startswith("hello"): 
        return "$0"
    elif greeting.startswith("h"):
        return "$20" 
    else: 
        return "$100"  

print(bank_greeting())