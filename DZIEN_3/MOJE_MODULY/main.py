#import dane
#import dane as dn
from dane import nrfilii as filia
from dane import book as bk
from funkcje.bfunkcja import czytaj_liste,czytaj_slownik
from klasy.Filia import Filia


print("_____________ dane ______________")
print(filia)
print(bk)

print("_____________ dane przez użycie funkcji ______________")
czytaj_liste(filia)
print("________")
czytaj_slownik(bk)

print("_____________ dane przez użycie klasy ______________")
f = Filia(6,"ABC","Złota 6 Kraków")
f.promocja(bk)
