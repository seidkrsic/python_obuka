

class Ljubimac: 
    # ime, vrsta, glad 
    def __init__(self, ime, vrsta): 
        self.ime = ime 
        self.vrsta = vrsta 
        self.glad = 5
    
    # metod nahrani 
    def nahrani(self):
        self.glad -= 3 
        if self.glad < 0: 
            self.glad = 0 
    
    # igraj_se 
    def igraj_se(self): 
        self.glad += 2 
        if self.glad > 10: 
            self.glad = 10 

    # status 
    def status(self): 
        if self.glad <3: 
            print(f"{self.ime} nije gladan") 
        elif self.glad <= 6: 
            print(f"{self.ime} je malo gladan.")
        else: 
            print(f"{self.ime} je jako gladan!") 


pas = Ljubimac("Willy", "Labrador") 
pas.status() 
pas.igraj_se() 
pas.status() 
pas.nahrani()
pas.nahrani() 
pas.status() 
print(pas.glad) 