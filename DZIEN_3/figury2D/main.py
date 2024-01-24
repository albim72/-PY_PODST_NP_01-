from prostokat import Prostokat
from trojkat import Trojkat

pr = Prostokat(4.4,6.7)
print(f'pole figury {pr.__class__.__name__} wynosi: {pr.policz_pole():.2f} cm2')

tr = Trojkat(5.8,7.2)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')
