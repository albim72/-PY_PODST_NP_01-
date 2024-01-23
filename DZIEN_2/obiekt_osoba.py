class Osoba:
    kolor_oczu = "brązowy"
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.info()
        
    def info(self):
        print("Utworzono nowy obiket klasy Osoba")
        
    def print_osoba(self):
        return (f"osoba -> {self.imie}, wiek [lata]: {self.wiek}, wzrost: {self.wzrost} cm,"
                f"waga: {self.waga} kg, kolor oczu: {self.kolor_oczu}")
    
    
    def wiek_za_n_lat(self,n):
        return self.wiek + n
    
    def czypracownik(self):
        return False
        
        
        
        
