liczby = [45,67,88,90,344,246,674,786,46,73,68,23,1,67,-100,0,88,-99,256,-456]

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum-minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    srarytm = suma_el/liczba_el
    return minimum,maksimum,rozstep,srarytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,sa = pokaz_statystyki(liczby)
print(f'maksimum: {maxi}, minimum: {mini}, rozstęp: {roz}, średnia: {sa}')
