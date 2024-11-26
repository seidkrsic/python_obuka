


""" 
{"name" : "Lasagna", "ingredients": [""]}
{"name" : "Cookie", "ingredients": [""]}
"""
recipes = [] 
unique_ingredients = set() # 
with open("recipes.txt", "r") as file: 
    for line in file: 
        row = line.strip().split(", ") 
        recipe = {"name" : row[0], "ingredients" : row[1:]} 
        recipes.append(recipe) 
        unique_ingredients.update(row[1:])  


print(len(unique_ingredients)) 
for recipe in recipes: 
    print(recipe)     

