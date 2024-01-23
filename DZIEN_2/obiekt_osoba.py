class Osoba:
    kolor_oczu = "brązowy"
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.info()

    def info(self):
        print("Utworzono nowy obiekt klasy Osoba")

    def print_osoba(self):
        return (f"osoba -> {self.imie}, wiek [lata]: {self.wiek}, wzrost: {self.wzrost} cm,"
                f"waga: {self.waga} kg, kolor oczu: {self.kolor_oczu}")


    def wiek_za_n_lat(self,n):
        return self.wiek + n

    def czypracownik(self):
        return False

print("*"*50)
p1 = Osoba("Jan",34,78,175)
print(f"kolor oczu: {p1.kolor_oczu}")
print(p1.print_osoba())
nlat = 3
print(f"wiek za {nlat} lata/a -> {p1.wiek_za_n_lat(nlat)} lata/a")
print(f"czy osoba jest pracownikiem? ({p1.czypracownik()})")

print("*"*50)
p2 = Osoba("Olga",29,56,169)
p2.kolor_oczu = "niebieskie"
print(f"kolor oczu: {p2.kolor_oczu}")
print(p2.print_osoba())
nlat = 8
print(f"wiek za {nlat} lata/a -> {p2.wiek_za_n_lat(nlat)} lata/a")
print(f"czy osoba jest pracownikiem? ({p2.czypracownik()})")

