class KlasaFormat:
    def __init__(self,wartosc):
        self.wartosc = wartosc

    def __format__(self, format_spec):
        if format_spec == 'd':
            return f'Wartość: {int(self.wartosc)}'
        elif format_spec == 'f':
            return f'Wartość: {float(self.wartosc)}'
        else:
            return f'Wartość: {self.wartosc}'

obiekt = KlasaFormat(42)
wynik = format(obiekt,'d')
wynik_f = f'{obiekt:d}'
print(wynik)
print(wynik_f)

obiekt = KlasaFormat(7)
wynik = format(obiekt,'d')
wynik_f = f'{obiekt:f}'
print(wynik)
print(wynik_f)
