import sys

try:
    f = open("mojedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
    # d = i / 0
except OSError as err:
    print(f"błąd systemowy: {err}")
except ValueError:
    print("nie można przekonwertować danych ze str na int")
except Exception as exx:
    print(f"znaleziono błąd: {exx}, typu: {type(exx)}")
    print(exx.args)
except:
    print(f"Nieoczekiwany błąd -> {sys.exc_info()[0]}")
