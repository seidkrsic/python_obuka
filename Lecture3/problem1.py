

food = { 
    "baja taco": 4.25,
    "burrito": 7.50, 
    "bowl": 8.50,
    "nachos": 11.00, 
    "quesadilla": 8.50,
    "super burrito": 8.50, 
    "super quesadilla": 9.50,
    "taco": 3.002,  # food["taco"] >>> 3.00
    "tortilla salad": 8.00
}

cost = 0 
while True: 
    try:
        user_input = input("Item (CTRL+D to quit)").lower() 
    except EOFError: 
        print("\nOrder completed") 
        print("-------------------")
        print(f"Cost: ${cost:.2f}") 
        break 
    
    if user_input in food:
        cost += food[user_input] 
        print(f"Total: ${cost:.2f}")     

    