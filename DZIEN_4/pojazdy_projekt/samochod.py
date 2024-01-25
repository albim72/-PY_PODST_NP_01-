from pojazd import Pojazd

class Samochod(Pojazd):
    def __init__(self, marka, model, rodzaj_silnika, rocznik, poj_bagaznika):
        super().__init__(marka, model, rodzaj_silnika, rocznik)
        self.poj_bagaznika = poj_bagaznika

    def __repr__(self):
        return f"reprezentacja tekstowa obiektu: {self.marka} {self.model}"

    def __str__(self):
        return (f"Samochód: {self.marka} {self.model}\n"
                f"rodzaj silnika: {self.rodzaj_silnika}\n"
                f"rocznik: {self.rocznik}\n"
                f"pojemność bagażnika: {self.poj_bagaznika} l")

    def spalanie(self, odl, jedn):
        return jedn*100*1.1/odl

    def koszt_przejazdu(self, odl, jedn, cena_j):
        return self.spalanie(odl,jedn)*(odl/100)*cena_j

