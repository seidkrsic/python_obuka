

from random import randint 


def main(): 
    level = get_level("Enter Level: ") 
    number = guess_number(level)
    while True: 
        guess = get_level("Guess number: ")  
        result = check_for_win(number, guess) 
        if result == 0: 
            print("Bravo majstore!!!") 
            break 
        elif result == -1: 
            print("Probaj malo veci broj.") 
        else: 
            print("Probaj malo manji broj.") 


def get_level(prompt): 
    while True: 
        try: 
            n = int(input(prompt)) 
            if n > 0: 
                return n 
            else: 
                print("Not valid number. Try positive number.")
        except ValueError: 
            print("Not valid number.") 


def guess_number(level): 
    return randint(1,level) 


def check_for_win(number, guess): 
    if number == guess: 
        return 0 
    elif number > guess: 
        return -1 
    else: 
        return 1 
    


main()
