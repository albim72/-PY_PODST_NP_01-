#krotka -> tuple

animal = ("pies","kot","papuga","królik","szczur","pies")

print(animal)
print(type(animal))

print(animal[1])
print(animal[2:4])

for a in animal:
    print(a)

print(animal.count("pies"))

if "papuga" in animal:
    print("tak, papuga to zwierz!")

if "budynek" not in animal:
    print("nie , budynek to nie zwierz!")

anim2 = ("pająk","ryba")

animal = animal + anim2

print(animal)

#zadanie - zmodyfikuj zadaną krotkę w następująacy sposób:
#1. Usuń wartość 453, zmodyfikuj wartość "Kraków" na "Toruń"
#2. Dodaj na pozycji 0 wartość 20

mojakrotka = tuple(("obiekt 56",False,453,78.455,"Kraków"))

print(mojakrotka)
mojalista = list(mojakrotka)
mojalista.remove(453)
pp = mojalista.index("Kraków")
mojalista[pp] = "Toruń"
mojalista.insert(0,20)
mojakrotka = tuple(mojalista)
print(mojakrotka)


samochod = ('audi Q7',3.8,2017,98000)
print(samochod)
mr = samochod[0]
print(mr)

print("___________________________")

(marka,poj,rok,cena) = samochod
print(marka)
print(poj)
print(cena)
print(rok)

opcje = 23,4,243,54.545

a,b,c,d = opcje
print(c)
print(type(opcje))
