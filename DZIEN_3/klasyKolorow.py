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

