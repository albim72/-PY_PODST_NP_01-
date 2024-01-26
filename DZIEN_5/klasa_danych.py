from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x=x

zlicz = Liczba(456)
print(zlicz)
print(zlicz.x)

#klasa danych
@dataclass
class DLiczba:
    x:int
    y:float=8.85

dlicz = DLiczba(7,2.2)
print(dlicz)
dwl = DLiczba(6)
print(dwl)
