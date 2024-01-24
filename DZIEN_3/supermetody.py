class KlasaA(object):
    def moja_funkcja(self):
        print("to jest metoda klasy KlasaA")

class KlasaB(KlasaA):
    def moja_funkcja(self):
        super().moja_funkcja()
        print("to jest metoda klasy KlasaB")

class KlasaC(KlasaB):
    def moja_funkcja(self):
        super().moja_funkcja()
        print("to jest metoda klasy KlasaC")


specj = KlasaC()
specj.moja_funkcja()
