

#
def number_of_vowels(string):
    count = 0
    string = string.lower() 
    for letter in string: 
        if letter in "aeiou": 
            count += 1 
    return count 


result = number_of_vowels("payetuhoon") 
print(result)  
