from dataclasses import dataclass,field
from typing import List

@dataclass
class Osoba:
    imie:str
    nazwisko:str
    wiek:int
    
@dataclass
class DzialFirmy:
    nazwa:str
    liczba_pracownikow:int
    
@dataclass
class Pracownik(Osoba):
    prac_id:int
    dzial:DzialFirmy
    doswiadczenie:List[str]=field(default_factory=list)
    
    def informacja_pracownik(self):
        print(f'Identyfikator pracownika: {self.prac_id}\n'
              f'Imię i nazwisko: {self.imie} {self.nazwisko}\n'
              f'Wiek: {self.wiek}\n'
              f'Dział Firmy: {self.dzial.nazwa}, liczba pracowników: {self.dzial.liczba_pracownikow}\n'
              f'Doświadczenie: {", ".join(self.doswiadczenie)}')
