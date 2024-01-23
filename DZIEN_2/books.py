class Book:
    #deklaracja stanu - konstruktor

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return "książka " + self.tytul + ", autor: " + self.autor


    def create_book(self):
        print("utworzenie nowej książki ")

    def rabat(self,procent):
        return self.cena*(procent/100)


bk = Book(34,"Wiedźmin","Andrzej Sapkowski",43)
print(bk)
print("Rabat: " + str(bk.rabat(22)) + " zł")
print("Kwota do zapłaty: " +str(bk.cena - bk.rabat(22)) + " zł")



