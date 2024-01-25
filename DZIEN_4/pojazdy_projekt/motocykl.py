from pojazd import Pojazd

class Motocykl(Pojazd):
    def __init__(self, marka, model, rodzaj_silnika, rocznik, typ):
        super().__init__(marka, model, rodzaj_silnika, rocznik)
        self.typ=typ

    def spalanie(self, odl, jedn):
        return jedn*100/odl

    def koszt_przejazdu(self, odl, jedn, cena_j):
        return self.spalanie(odl,jedn)*(odl/100)*cena_j
