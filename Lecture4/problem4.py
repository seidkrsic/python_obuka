

food = { 
    "apple" : 130, 
    "avocado" : 50, 
    "banana" : 110, 
    "lemon" : 50, 
    "orange" : 80
}

def main(): 
    x = input("Food: ") 
    if x in food:
        print(food[x], "calories.") 
    else: 
        print("Not available.")

main()