


def categorize_vehicle(weight, wheels): 
    # dva tocka i manje od 350kg --- motor 
    if wheels == 2 and weight < 350: 
        return "motor" 
    # 4 tocka i izmedju 351kg i 3500kg --- automobil 
    elif wheels == 4 and 351 < weight < 3500: 
        return "automobil"
    # 4 tocka i > 3500kg -- kombi 
    elif wheels == 4 and weight > 3500: 
        return "kombi"
    # > od 4 tocka i > 3500kg --- kamion 
    elif wheels > 4 and weight > 3500: 
        return "kamion"
    # nista od navedenog --- los unos. 
    else: 
        return "los unos" 
print(categorize_vehicle(4000, 6)) # >>> automobil 