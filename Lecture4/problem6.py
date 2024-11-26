
"""
level: 1
1+4=5   # score += 1 
2+6=7
EEE
2+6=2
EEE 
2+6=10
EEE
2+6=8 
4+9= 

"""

# Score je: 9/10 
import random 

def main(): 
    score = 0 
    level = get_level() 

    for i in range(10): 
        question, answer = generate_question(level) 
        correct = False 
        attempts = 0 
        while attempts < 3 and not correct: 
            print(question, end="") 
            try: 
                guess = int(input()) 
                if guess == answer: 
                    correct = True 
                    score += 1 
                elif guess < answer: 
                    print("EEE") 
                else: 
                    print("EEE")  
            except ValueError: 
                print("EEE")
            attempts += 1  

        if not correct:  # not False > True 
            print(f"{question}{answer}") 
            
    print(f"Score: {score}/10") 



def get_level(): 
    while True: 
        try: 
            n = int(input("Enter level: ")) 
            if n in [1,2,3]: 
                return n 
        except ValueError: 
            print("Invalid input. Please enter a number between 1 and 3.")


def generate_question(level):
    if level == 1: 
        x = random.randint(0,9) 
        y = random.randint(0,9) 
    elif level == 2: 
        x = random.randint(10,99) 
        y = random.randint(10,99) 
    elif level == 3: 
        x = random.randint(100,999) 
        y = random.randint(100,999)   
    result = x + y 
    return f"{x}+{y}=", result  

main()