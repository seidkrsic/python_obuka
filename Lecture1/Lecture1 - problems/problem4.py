

def is_negative(number):
    if number < 0: 
        return True 
    else: 
        return False 


def better_is_negative(number): 
    return number < 0  # True 

print(better_is_negative(10))