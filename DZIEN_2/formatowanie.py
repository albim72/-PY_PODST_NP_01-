tekst = "to jest test!"
cyfra = 8
nr = 8897

info = "informacja nr {2}: {0}, wybrana cyfra: {1}"
#ekstrapolacja wartości string 'teskt' wewnątrz wartośc 'info' -> {}

print(info.format(tekst,cyfra,nr))


print("___________________________________________________________")

print("wstrzykiwanie ciągów string")

fr_key = 'moja_wartosc'
fr_value = 2.7654635

fr = '%-30s = %.2f' %(fr_key,fr_value)
print(fr)

print("*"*50)

owoce = [
    ('awokado',8.99),
    ('banan',6.23),
    ('mandarynka',9.9),
    ('jabłko',4.26),
    ('granat',5.66),
    ('ananas',12)
]

print("________ enumerate __________")
nb = [4,2,5,2,6,32,6,3,7,3]
for x in nb:
    print(nb.index(x),":",x)

print("_____")

print(list(enumerate(nb)))

for i,v in enumerate(nb):
    print(i, "->",v)

print("_________ CENNIK OWOCÓW nr 1 _________")
for i,(item,wart) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(i,item,wart))

print("_________ CENNIK OWOCÓW nr 2 _________")
for i,(item,wart) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(
        i+1,
        item.title(),
        round(wart,1)
    ))

print("_______________________________________________")
# formatowanie f-string
imie = "Jan"
wiek = 50

print(f'Witaj, twoje imię to {imie}, masz {wiek} lat')

wart = 4.65432543647
print(f'wartość w = {wart:.2f}')

numer = 435
print(f'identyfikator: {numer:05d}')

from datetime import datetime
from colorama import Fore
data = datetime.now()

print(f'dzisiaj jest {Fore.RED}{data: %Y-%m-%d, godzina:%H:%M:%S}{Fore.RESET}')

x = 5
y = 104

print(f"suma a({x})+b({y}) = \033[1m{x+y}\033[0m")
