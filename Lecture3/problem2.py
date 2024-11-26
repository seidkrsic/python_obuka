


def main(): 
    user_input = input("Input fraction X/Y: ") 
    try:
        result = convert(user_input)   # 1, ... 100
    except ValueError as error: 
        print(error) 
    except ZeroDivisionError as error: 
        print(error) 
    else: 
        final_result = final_convert(result)  # 
        print(final_result)     


def convert(value): 
    x, y = value.split("/")
    try:
        x, y = int(x), int(y) 
    except ValueError: 
        raise ValueError("X or Y not integers.") 

    if y == 0:  
        raise ZeroDivisionError("cannot divide by zero.")
    if x > y : 
        raise ValueError("X is greater than Y.") 
    
    return round((x/y)*100) 


def final_convert(value): 
    if value <= 1: 
        return "E" 
    elif value >= 99: 
        return "F" 
    else: 
        return f"{value}%" 

main() 