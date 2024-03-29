class Book:
    #deklaracja stanu - konstruktor

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    wydawnictwo:str

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return "książka " + self.tytul + ", autor: " + self.autor + ", oprawa:" + self.oprawa

    def get_oprawa(self):
        return self.oprawa


    def set_oprawa(self,nowaoprawa):
        self.oprawa = nowaoprawa


    def create_book(self):
        print("utworzenie nowej książki ")

    def rabat(self,procent):
        return self.cena*(procent/100)

    def set_wydawnictwo(self,nowew):
        self.wydawnictwo = nowew

    def get_wydawnictwo(self):
        return self.wydawnictwo


bk = Book(34,"Wiedźmin","Andrzej Sapkowski",43)
print(bk)
print("Rabat: " + str(bk.rabat(22)) + " zł")
print("Kwota do zapłaty: " +str(bk.cena - bk.rabat(22)) + " zł")
bk.set_oprawa("twarda")

print('zmiana oprawy na: ' + bk.get_oprawa())
bk.set_wydawnictwo("ABC")
print("wydawnicto " + bk.get_wydawnictwo())

#stwórz drugi obiekt klasy Book

print("____________________________________________________")

bk2 = Book(67,"Hobbit","J.R.R. Tolkien",39.8)
print(bk2)
print("Rabat: " + str(bk2.rabat(16)) + " zł")
print("Kwota do zapłaty: " +str(bk2.cena - bk2.rabat(16)) + " zł")
bk2.set_oprawa("tekturowa")

print('zmiana oprawy na: ' + bk2.get_oprawa())
bk2.set_wydawnictwo("Romcio")
print("wydawnicto " + bk2.get_wydawnictwo())


