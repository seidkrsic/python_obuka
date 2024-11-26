

# exceptions u Pythonu 
def main(): 
    x = get_int("Unesi broj: ") 
    print(f"x is {x}") 


def get_int(prompt):
    while True: 
        try:
            return int(input(prompt)) 
        except ValueError: 
            pass 

    
 
main() 