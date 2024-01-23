print((lambda a:a+10)(45))
print((lambda a:a+10)(55.86))

dodaj = lambda x,y:x+y
wynik = dodaj(4,7)
print(wynik)

def potega(n):
    return lambda a:a**n

wynik = potega(6)(9)
print(wynik)

liczby = [8,3,6,12,-4,0,34,113,-45,98,13,2,-5,-66,70,-49,221,3,5]

parzste = list(filter(lambda x:x%2==0,liczby))
print(parzste)

def ujemne(x):
    return x<0

ujem = list(filter(ujemne,liczby))
print(ujem)

cube = list(map(lambda x:x**3,liczby))
print(cube)

#list comprehension

kwadraty = [x**2 for x in range(25)]
print(kwadraty)

lparz = [x for x in liczby if x%2==0]
print(lparz)

slowa = ['jabłko','piarg','koń','nosorożec','olej','rabarbar','złoto','ogromny']

krotkie_slowa = [slowo for slowo in slowa if len(slowo)<6]
print(krotkie_slowa)

#przykład - funkcje złożone
def podnies_do_kwadratu(x):
    return x**2

def pomnoz_przez_dwa(y):
    return y*2

def policz_calosc(x):
    return pomnoz_przez_dwa(podnies_do_kwadratu(x))

wynik = policz_calosc(4)
print(wynik)

def policz_calosc_rev(x):
    return podnies_do_kwadratu(pomnoz_przez_dwa(x))


wynik = policz_calosc_rev(4)
print(wynik)
