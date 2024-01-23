class KlasaPierwsza:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def print_ab(self):
        print(f"a={self.a}, b={self.b}")
        
        
class DrugaKlasa(KlasaPierwsza):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
        
    def print_abc(self):
        print(f"a={self.a}, b={self.b}, c={self.c}")
        
    def policzsume(self):
        print(f"suma a+b+c={self.a + self.b + self.c}")
