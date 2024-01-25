class Licznik:
    def __init__(self):
        self.licznik = 0

    def __call__(self):
        self.licznik += 1
        return self.licznik


l_obj = Licznik()

for _ in range(11):
    wynik = l_obj()
    print(f'aktualna wartość licznika: {wynik}')
