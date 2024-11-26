

# 

def deep_question(): 
    """ 
    input ---> what's the answer to everything?
    42 ili forty-two ili forty two ---> YES 
    inace ---> NO 
    .lower() 
    """
    answer = input("what's the answer to everything? ").lower() 
    if answer == "42" or answer == "forty-two" or answer == "forty two": 
        print("YES")
    else: 
        print("NO") 


deep_question()