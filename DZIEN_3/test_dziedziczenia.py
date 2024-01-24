class Pierwsza:
    def __init__(self,a):
        self.a=a

    def policz(self):
        return self.a*9

class Druga(Pierwsza):
    def __init__(self, a, b):
        super().__init__(a)
        self.b=b

class H:
    def __init__(self,n):
        self.n=n

class Trzecia(Druga,H):

    def __init__(self, a, b, n):
        Druga.__init__(self,a, b)
        H.__init__(self,n)

    def policz(self):
        return super().policz() + self.n*2 + self.b

print("Jak sprawdzić dzidziczenie klas??")
print(f"Czy klasa Druga dziedziczy Pierwsza? {issubclass(Druga,Pierwsza)}")
print(f"Czy klasa Trzecia dziedziczy Pierwsza? {issubclass(Trzecia,Pierwsza)}")
print(f"Czy klasa H dziedziczy Pierwsza? {issubclass(H,Pierwsza)}")

