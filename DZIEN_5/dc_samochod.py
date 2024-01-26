from dataclasses import dataclass

@dataclass
class Car:
    marka:str
    model:str
    rok:int
    kolor:str

    def get_kolor(self):
        return self.kolor

    def set_kolor(self,nowykolor):
        self.kolor = nowykolor

car1 = Car("Toyota","Avensis",2020,"biały")
print(car1)

car2 = Car("Jeep","Cherokee",2016,"szary metallic")
print(car2)
car2.set_kolor("czarna perła")
print(f'kolor po zmianie: {car2.get_kolor()}')
