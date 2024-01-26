from dataclasses import dataclass

@dataclass
class Article:
    title:str
    content:str
    author:str


@dataclass(init=False)
class PyArticle(Article):
    language:str
    author:str
    price:int=30

    def __init__(self,title,price):
        self.title=title
        self.price=price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "opis wybranych aspektów użycia języka Python"

    def rabat(self,procent):
        print(f'Publikacja {self.title}, autor: {self.author}, cena bazowa: {self.price} zł, '
              f'cena po rabacie: {(1-procent/100)*self.price} zł')

art1 = PyArticle("Algorytmiczna Teoria Gier w Pythonie",120)
print(art1)
art1.rabat(23)
