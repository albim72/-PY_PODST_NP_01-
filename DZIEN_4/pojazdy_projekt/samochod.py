from pojazd import Pojazd

class Samochod(Pojazd):
    def __init__(self, marka, model, rodzaj_silnika, rocznik, poj_bagaznika):
        super().__init__(marka, model, rodzaj_silnika, rocznik)
        self.poj_bagaznika = poj_bagaznika

    def spalanie(self, odl, jedn):
        return jedn*100*1,1/odl

    def koszt_przejazdu(self, odl, jedn, cena_j):
        return self.spalanie(odl,jedn)*(odl/100)*cena_j
