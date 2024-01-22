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

