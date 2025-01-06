

# Sistem za upravljanje Bibliotekom 

class Biblioteka: 
    def __init__(self):
        self.knjige = [] 
        self.clanovi = [] 

    # dodaj_knjigu 
    def dodaj_knjigu(self, knjiga): 
        self.knjige.append(knjiga) 
        print(f"Dodata knjiga {knjiga.naslov} u biblioteku.") 

    # registruj clana 
    def registruj_clana(self, clan):  # clan je objekat iz klase ClanBiblioteke
        for member in self.clanovi: 
            if member.broj_clanske_karte == clan.broj_clanske_karte: 
                print("Doslo je do greske. Clan sa ovim brojem vec postoji.") 
                return 
        self.clanovi.append(clan) 
        print(f"Clan {clan.ime} {clan.prezime} je uspjesno dodat.") 
    
    # pronadji knjigu po naslovu 
    def pronadji_knjigu_po_naslovu(self, naslov): # naslov - je samo string "Na Drini cuprija"
        for knjiga in self.knjige: 
            if knjiga.naslov == naslov: 
                print("Knjiga PRONADJENA!!!")
                return knjiga 
        print(f"Knjiga sa naslovom '{naslov}' nije pronadjena.") 
        return 




class ClanBiblioteke: 
    def __init__(self, ime, prezime, broj_clanske_karte):
        self.ime = ime 
        self.prezime = prezime 
        self.broj_clanske_karte = broj_clanske_karte 
        self.pozajmljene_knjige = [] 
    
    def pozajmi_knjigu(self, knjiga): 
        if knjiga.dostupna: 
            knjiga.pozajmi() 
            self.pozajmljene_knjige.append(knjiga) 
        else: 
            print("Knjiga nije dostupna. Probaj kasnije.") 

    def vrati_knjigu(self,knjiga): 
        if knjiga in self.pozajmljene_knjige: 
            knjiga.vrati() 
            self.pozajmljene_knjige.remove(knjiga) 
        else: 
            print(f"Ovu knjigu niste vi iznajmili. Doslo je do greske.") 
    


class Knjiga: 
    def __init__(self, naslov, autor):
        self.naslov = naslov
        self.autor = autor 
        self.dostupna = True 

    def __str__(self):
        return f"{self.naslov} - {self.autor}" 

    def pozajmi(self): 
        if self.dostupna: 
            self.dostupna = False 
            print(f"Knjiga {self.naslov} je uspjesno pozajmljena.") 
        else: 
            print("Knjiga je vec iznajmljena.") 

    def vrati(self): 
        self.dostupna = True 
        print(f"Knjiga {self.naslov} je vracena.") 
    

# ovo tek kad implementiramo ove klase iznad 
biblioteka = Biblioteka()

knjiga1 = Knjiga("Na Drini Cuprija", "Ivo Andric") 
knjiga2 = Knjiga("Gorski Vijenac", "Petar II Petrovic NJegos") 

clan_biblioteke = ClanBiblioteke("Petar", "Markovic", "12345")
clan_biblioteke2 = ClanBiblioteke("Marko", "Markovic", "54321")

biblioteka.dodaj_knjigu(knjiga1) 
biblioteka.dodaj_knjigu(knjiga2) 

biblioteka.registruj_clana(clan_biblioteke)
biblioteka.registruj_clana(clan_biblioteke2) 
x = biblioteka.pronadji_knjigu_po_naslovu("Na Drini Cuprija") 
