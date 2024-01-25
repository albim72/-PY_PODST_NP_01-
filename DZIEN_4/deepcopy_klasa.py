import copy

class MojaKlasa:
    def __init__(self,nazwa):
        self.nazwa = nazwa

    def __deepcopy__(self, memo):
        print(f'tworzenie głębokiej kopii obiektu: {self.nazwa}')
        nowy_obiekt = self.__class__(self.nazwa)
        memo[id(self)] = nowy_obiekt
        return nowy_obiekt

oryginal = MojaKlasa("jakaśtamopcja")
skopiowany = copy.deepcopy(oryginal)
print(oryginal)
print(skopiowany)
