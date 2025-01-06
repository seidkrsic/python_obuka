

# racun treba da ima sljedece atribute: broj_racuna, vlasink, pocetno_stanje=0 

class BankovniRacun: 
    def __init__(self, broj_racuna, vlasnik, pocetno_stanje=0):
        self.broj_racuna = broj_racuna
        self.vlasnik = vlasnik 
        self.stanje = pocetno_stanje 
    
    # method - uplata - ima argument (int) ---- povecava stanje na racunu korisnika za onoliko 
    # novca koliko unesemo kao argument 

    def uplata(self, novac): 
        if novac > 0: 
            self.stanje += novac 
            print("Uplata uspjesna.") 
        else: 
            print("Uplata mora biti vise od 0 eura.") 

    # isplata za onoliko para koliko unesemo kao argument 
    def isplata(self, novac): 
        if self.stanje >= novac: 
            self.stanje -= novac 
            print("Isplata uspjesna.") 
        else: 
            print("Nema dovoljno sredstava.") 

    def transfer(self, drugi_racun, iznos): 
        if iznos <=0: 
            print("Iznos transfera mora biti veci od 0 eura.") 
            return 
        if iznos > self.stanje: 
            print("Nemate dovoljno sredstava.") 
            return 
        self.stanje -= iznos 
        drugi_racun.stanje += iznos 
        print("Transfer novca uspjesan.")
        

racun1 = BankovniRacun("111-222", "Marko Markovic") 
racun2 = BankovniRacun("222-333", "Jovana Jovanovic", 200) 

racun2.transfer(racun1, 100) 
print(racun2.stanje) 
print(racun1.stanje) 
