def tylko_liczby_dodatnie(liczba):
    if liczba < 0:
        raise ValueError("Liczba powinna być nieujemna!")
    else:
        print(f"liczba jest nieujemna i wynosi: {liczba}")

try:
    nb = int(input("Podaj wartość liczby n: "))
    tylko_liczby_dodatnie(nb)
except ValueError as ve:
    print(f"wystąpił błąd: {ve}")
    # raise

def podaj_imie(imie):
    if imie == "Jan":
        raise ValueError("Imię Jan nie wchodzi w grę!")
    return f'Twoje imię to {imie}'

try:
    i = input("podaj swoje imię: ")
    print(podaj_imie(i))
except ValueError as v:
    print(v)
    raise 

