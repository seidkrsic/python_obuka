

class Vault:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons 
        self.sickles = sickles 
        self.knuts = knuts 

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other): 
        galleons = self.galleons + other.galleons 
        sickles = self.sickles + other.sickles 
        knuts = self.knuts + other.knuts 
        return Vault(galleons, sickles, knuts) 
    
# 1 + 2i + (3+4i) = 4 + 6i  


potter = Vault(100, 50, 25) 
print(potter) 
weasley = Vault(25, 50, 100) 
print(weasley) 
print("RESULT: ") 
total = potter + weasley 
print(total) 
