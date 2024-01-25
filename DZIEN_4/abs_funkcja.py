class Liczba:
    def __init__(self,wartosc):
        self.wartosc = wartosc

    def __abs__(self):
        return abs(self.wartosc*3)


lb = Liczba(-11)

wynik = abs(lb)
print(f"Wartości bezwzględna trzykrotności liczby: {wynik}")
