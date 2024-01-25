def dzielenie(x,y):
    try:
        wynik=x/y
    except ZeroDivisionError as zd:
        print(f"Dzielenie przez 0! ({zd})")
    except NameError as ne:
        print(ne)
    except Exception as exc:
        print(exc)
    else:
        print(f"wynik dzielenia: {wynik}")
    finally:
        print("policzmy coś jeszcze")

try:
    dzielenie(5,6)
    dzielenie(5,0)
    dzielenie(0,0)
    dzielenie(0,1)
    dzielenie(0.000655,233)
    dzielenie(-88.2,True)
    dzielenie(6,"fgd")
    dzielenie(678)
except TypeError as tp:
    print(tp)
