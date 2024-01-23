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

class KlasaSpecjalna:
    def __init__(self,g):
        self.g=g

class TrzeciaKlasa(DrugaKlasa,KlasaSpecjalna):
    def __init__(self, a, b, c, d, g):
        DrugaKlasa.__init__(self,a, b, c)
        KlasaSpecjalna.__init__(self,g)
        self.d=d

    def print_abcdg(self):
        print(f"a={self.a}, b={self.b}, c={self.c}, d={self.d}, g={self.g}")

    def policzsume(self):
        print(f"suma a+b+c+d+g={self.a + self.b + self.c+self.d+self.g}")


print("________ KlasaPierwsza _________")

pk = KlasaPierwsza(34,101)
pk.print_ab()

print("________ KlasaDruga _________")
dk = DrugaKlasa(6,17,88)
dk.print_ab()
dk.print_abc()
dk.policzsume()

print("________ KlasaTrzecia _________")
tk = TrzeciaKlasa(45,23,8,79,11)
tk.print_ab()
tk.print_abc()
tk.print_abcdg()
tk.policzsume()

