from abc import ABC,abstractmethod

class Pojazd(ABC):
    def __init__(self,marka,model,rodzaj_silnika,rocznik):
        self.marka = marka
        self.model = model
        self.rodzaj_silnika = rodzaj_silnika
        self.rocznik = rocznik


    @abstractmethod
    def spalanie(self,odl,jedn):
        pass


    @abstractmethod
    def koszt_przejazdu(self,odl,jedn,cena_j):
        pass




