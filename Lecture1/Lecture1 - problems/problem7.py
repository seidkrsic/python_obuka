


def cost_project(engraving, solid_gold): 
    """ 
    prsten od zlata --- 100$ 
    prsten pozlacen --- 50$ 
    cijena gravure: 
    prsten od zlata --- 1 karakter  - 10$ python
    prsten pozlacen --- 1 karakter  - 7$ python
    returns cost_of_project 
    cost_project("python", True/False) 
    124$ 
    """
    if solid_gold: 
        cost = 100 + 10*len(engraving) 
    else: 
        cost = 50 + 7*len(engraving) 
    return cost 

print(cost_project("i love you", False)) # >>> 100$  



