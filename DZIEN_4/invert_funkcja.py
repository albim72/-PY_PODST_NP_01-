class KlasaInvert:
    def __init__(self,liczba):
        self.liczba=liczba

    def __invert__(self):
        return ~self.liczba

obiekt = KlasaInvert(5)
wynik = ~obiekt

print(f"wynik operacji ~ : {wynik}")

obiekt = KlasaInvert(False)
wynik = ~obiekt

print(f"wynik operacji ~ : {wynik}")

# obiekt = KlasaInvert(7.7)
# wynik = ~obiekt
# 
# print(f"wynik operacji ~ : {wynik}")
