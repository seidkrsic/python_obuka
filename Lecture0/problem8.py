

def hide_bank_card_number(card_number): 
    return "*"*(len(card_number) - 4) + card_number[-4:] 

result = hide_bank_card_number("123456789012") 
print(result) # ********9012


