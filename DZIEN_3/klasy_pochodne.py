class Base(object):
    def __init__(self,imie):
        self.imie=imie

    def get_imie(self):
        return self.imie


class Child(Base):
    def __init__(self, imie, wiek):
        super().__init__(imie)
        self.wiek=wiek

    def get_wiek(self):
        return self.wiek


class GrandChild(Child):

    def __init__(self, imie, wiek, miasto):
        super().__init__(imie, wiek)
        self.miasto = miasto

    def __repr__(self):
        return (f"Wnuczek(GrandChild):\nimię -> {self.get_imie()}\nwiek -> {self.get_wiek()}\n"
                f"miasto -> {self.get_miasto()}")

    def get_miasto(self):
        return self.miasto


ob = GrandChild("Bonifacy",19,"Kraków")
print(ob)
print(f'dane osoby -> imię: {ob.get_imie()}, wiek: {ob.get_wiek()}, miasto: {ob.get_miasto()}')

print("_____________________________________________________")
ob2 = GrandChild("Olga",33,"Lublin")
print(ob2)
