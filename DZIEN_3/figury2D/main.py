from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

pr = Prostokat(4.4,6.7)
print(f'pole figury {pr.__class__.__name__} wynosi: {pr.policz_pole():.2f} cm2')

tr = Trojkat(5.8,7.2)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')

trp = Trapez(8.2,5.4,4.4)
print(f'pole figury {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm2')

kl = Kolo(5.5)
print(f'pole figury {kl.__class__.__name__} wynosi: {kl.policz_pole():.2f} cm2')
