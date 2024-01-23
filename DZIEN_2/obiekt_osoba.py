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


    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi() < 18.5:
            return 'niedowaga'
        elif self.bmi() <=25:
            return 'waga prawidłowa'
        elif self.bmi() <= 30:
            return 'nadwaga'
        elif self.bmi() <= 35:
            return 'otyłość stopnia I'
        elif self.bmi() <= 40:
            return 'otyłość stopnia II'
        else:
            return 'otyłość stopnia III'
        
       
    def policz_ppm(self,plec):
        if plec == "K":
            return 655.1 + 9.563*self.waga + 1.85*self.wzrost - 4.676*self.wiek
        elif plec == "M":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wieku  
        else:
            return "nie ma takiej płci"
            

print("*"*50)
p1 = Osoba("Jan",34,78,175)
print(f"kolor oczu: {p1.kolor_oczu}")
print(p1.print_osoba())
nlat = 3
print(f"wiek za {nlat} lata/a -> {p1.wiek_za_n_lat(nlat)} lata/a")
print(f"czy osoba jest pracownikiem? ({p1.czypracownik()})")
print(f"bmi ciała wynosi: {p1.bmi():.2f}, opis: {p1.opis_bmi()}")

print("*"*50)
p2 = Osoba("Olga",29,56,169)
p2.kolor_oczu = "niebieskie"
print(f"kolor oczu: {p2.kolor_oczu}")
print(p2.print_osoba())
nlat = 8
print(f"wiek za {nlat} lata/a -> {p2.wiek_za_n_lat(nlat)} lata/a")
print(f"czy osoba jest pracownikiem? ({p2.czypracownik()})")

class Pracownik(Osoba):

    def __init__(self, imie, wiek, waga, wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie, wiek, waga, wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        return (f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, "
                f"lata pracy: {self.latapracy}, wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True

print("*"*50)
o1 = Pracownik("Aneta",45,72,170,"ABC","Dyrektor",12,12300)
o1.kolor_oczu = "zielone"
print(f"kolor oczu: {o1.kolor_oczu}")
print(o1.print_osoba())
print(o1.print_pracownik())
nlat = 11
print(f"wiek za {nlat} lata/a -> {o1.wiek_za_n_lat(nlat)} lata/a")
print(f"czy osoba jest pracownikiem? ({o1.czypracownik()})")
print(f"bmi ciała wynosi: {o1.bmi():.2f}, opis: {o1.opis_bmi()}")


class Ekstra:
    pass

class Sport:
    def __init__(self,dyscyplina,lataupr,best_wynik):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.best_wynik = best_wynik

    def infosport(self):
        return f"dysycyplina: {self.dyscyplina}, czas uprawiania [lata]: {self.lataupr}, życiówka: {self.best_wynik}"

class Student(Pracownik,Sport,Ekstra):

    def __init__(self, imie, wiek, waga, wzrost, nr_studenta,wydzial,rok_stud,
                 firma="", stanowisko="", latapracy="", wynagrodzenie="",dyscyplina="",lataupr="",best_wynik=""):
        Pracownik.__init__(self,imie, wiek, waga, wzrost, firma, stanowisko, latapracy, wynagrodzenie)
        Sport.__init__(self,dyscyplina,lataupr,best_wynik)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.rok_stud = rok_stud

    def print_student(self):
        return f"student nr {self.nr_studenta}, wydział: {self.wydzial}, rok studiów: {self.rok_stud}"

    def czypracownik(self):
        return self.firma != ""


print("*"*50)
s1 = Student("Olaf",22,77,174,454534,"Budowlany",3)
print(s1.print_osoba())
print(s1.print_student())
nlat = 6
print(f"wiek za {nlat} lata/a -> {s1.wiek_za_n_lat(nlat)} lata/a")
print(f"czy student jest pracownikiem? ({s1.czypracownik()})")


print("*"*50)
s2 = Student("Anna",23,60,171,978778,"Automatyki i Informatyki",4,
             "XYZ","sekretarka",1,3300)
print(s2.print_osoba())
print(s2.print_student())
print(s2.print_pracownik())
nlat = 4
print(f"wiek za {nlat} lata/a -> {s2.wiek_za_n_lat(nlat)} lata/a")
print(f"czy student jest pracownikiem? ({s2.czypracownik()})")

#utwórz instancję klasy Student s3, studeny nie jest pracownikiem, ale jest sportowcem, użyj dostepnych metod!
print("*"*50)
s3 = Student("Robert",22,80,179,2343545,"Nauk Społecznych",3,
             dyscyplina="niegi górskie ultra",lataupr=6,best_wynik="70km, 11h 2min 3s")
print(s3.print_osoba())
print(s3.print_student())
print(s3.infosport())
nlat = 17
print(f"wiek za {nlat} lata/a -> {s3.wiek_za_n_lat(nlat)} lata/a")
print(f"czy student jest pracownikiem? ({s3.czypracownik()})")
print(f"bmi ciała wynosi: {s3.bmi():.2f}, opis: {s3.opis_bmi()}")


