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
        
    def get_miasto(self):
        return self.miasto
    
