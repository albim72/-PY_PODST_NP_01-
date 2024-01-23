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
