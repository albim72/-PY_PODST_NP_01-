#Utwórz klasę dziedzącą jawnie klasę object o nazwie PaletaKolorow(idpalety,liczba_kolorow,nazwa_palety)
#Utwórz konstruktor klasy uwzględniając dane powyżej -: def __init__()
#Utwórz metodę get_liczba_kolorow() - zwracającą liczbę kolorów palety
#Utwórz metodę print_paleta - która wypisze dane palety - id,nazwa

#Utwórz obiekt plt1 i użyj dostępnych metod na obiekcie

class PaletaKolorow(object):

    def __init__(self,idpalety,liczba_kolorow,nazwa_palety):
        self.idpalety = idpalety
        self.liczba_kolorow = liczba_kolorow
        self.nazwa_palety = nazwa_palety

    def get_liczba_kolorow(self):
        return self.liczba_kolorow

    def print_paleta(self):
        return f'Paleta nr {self.idpalety}, nazwa: {self.nazwa_palety}'

plt1 = PaletaKolorow(45,100,"Setka")
print(f'liczba kolorów w palecie: {plt1.get_liczba_kolorow()}')
print(plt1.print_paleta())


#Stwórz klasę Kolory dziedziczącą klasę PaletaKolorow,
#zbuduj konstruktor z dziedziczeniem oparty na konstruktorze klasy PaletaKolorow i uzupełnij go
#o pola: id_koloru, nazwa_koloru
#dodaj metodę print_kolor i wypisz za jej pomocą dane: id_koloru, nazwa_koloru
#zbuduj obiekty k1 i k2 opisujące dwa równe kolory - użyj wszstkich dostępnych metod dla tych instancji

class Kolory(PaletaKolorow):
    def __init__(self, idpalety, liczba_kolorow, nazwa_palety, id_koloru, nazwa_koloru):
        super().__init__(idpalety, liczba_kolorow, nazwa_palety)
        self.id_koloru = id_koloru
        self.nazwa_koloru = nazwa_koloru

    def print_kolor(self):
        return f'id koloru: {self.id_koloru}, nazwa koloru: {self.nazwa_koloru}'

k1 = Kolory(12,90,"S10",34,"czerwony")
print("___ kolor k1 ____")
print(f'liczba kolorów w palecie: {k1.get_liczba_kolorow()}')
print(k1.print_paleta())
print(k1.print_kolor())


k2 = Kolory(555,255,"specjalna",80,"biały")
print("___ kolor k2 ____")
print(f'liczba kolorów w palecie: {k2.get_liczba_kolorow()}')
print(k2.print_paleta())
print(k2.print_kolor())

