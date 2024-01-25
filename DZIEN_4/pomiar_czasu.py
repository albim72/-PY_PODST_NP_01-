import timeit

def funkcja_z_pomiarem():
    suma = 0
    for i in range(10_000_000):
        suma += 2*i
    return suma

nt = 15
czas_wykonania_jedn = timeit.timeit(funkcja_z_pomiarem,number=1)
czas_wykonania = timeit.timeit(funkcja_z_pomiarem,number=nt)
print(f'czas pierwszego wykonania funkcji: {czas_wykonania_jedn} s')
print(f'czas wykonania operacji: {czas_wykonania} s')
print(f'średni czas wykonania funkcji: {czas_wykonania/nt} s')
