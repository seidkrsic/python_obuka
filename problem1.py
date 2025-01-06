


# Implementirati klasu Tacka. 

# (1,2) 
import math 

class Tacka:
    def __init__(self,x, y):
        self.x = x  
        self.y = y 

    def __str__(self):
        return f"({self.x},{self.y})" 

    # metod koji racuna udaljenost tacke od koordinatnog pocetka 
    def udaljenost_od_koordinatnog_pocetka(self): 
        # korijen iz (x^2+y^2) 
        result = math.sqrt((self.x)**2 + (self.y)**2) 
        return round(result,2) 

    def udaljenost_od_druge_tacke(self, druga_tacka): 
        # korijen iz ((prvax-drugax)**2 + (pravay-drugay)**2) 
        result_x = self.x - druga_tacka.x 
        result_y = self.y - druga_tacka.y 
        result = math.sqrt(result_x**2+result_y**2) 
        return result 
    

tacka_A = Tacka(0,0) # x, y 
tacka_B = Tacka(1,1) 
# print(tacka_A.udaljenost_od_koordinatnog_pocetka())   
# print(tacka_B.udaljenost_od_koordinatnog_pocetka()) 
x = tacka_A.udaljenost_od_druge_tacke(tacka_B) 
print(x) 