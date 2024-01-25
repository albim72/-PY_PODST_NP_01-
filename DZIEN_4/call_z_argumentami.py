class Kalkulator:
    def __call__(self,x,y):
        suma = x+y
        roznica = x-y
        iloczyn = x*y
        print(f"x={x}, y={y} -> suma x+y = {suma}, różnica x-y = {roznica}, iloczyn x*y = {iloczyn}")


k = Kalkulator()
k(7,5)
