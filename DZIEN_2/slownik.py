#słownik -> doctionary => (klucz,wartość)

pojazd = {
    "marka":"Ford",
    "model":"Mustang",
    "rok":1965,
    "kolor":"czerwony",
    455:6745634
}

print(pojazd)
print(type(pojazd))

print(pojazd["marka"])

mg = pojazd.get("model")
print(mg)

pojazd["kolor"]="śliwka"

print(pojazd)

pojazd["przebieg"] = 145600
print(pojazd)

print(len(pojazd))

#zwracanie listy kluczy słownika
print(pojazd.keys())
#zwracanie listy wartości słownika
print(pojazd.values())
#zwracanie elementów słownika
print(pojazd.items())

#wyświetlanie iteracyjnie struktur słownika
print("________ klucze słownika __________")
for x in pojazd:
    print(x)

print("________ wartości  słownika I __________")

for y in pojazd:
    print(pojazd[y])
print("________ wartości  słownika II __________")

for y in pojazd.values():
    print(y)

print("________ elementy  słownika  __________")

for x,y in pojazd.items():
    print(x," : ",y)

autokomis = {
    "auto1":{
                "marka":"Ford",
                "model":"Mustang",
                "rok":1965,
                "kolor":["czerwony","burgund"]
    },
    "auto2":{
                "marka":"Jeep",
                "model":"Cherokee",
                "rok":2018,
                "kolor":["czarny","biały","zielony"]
    },
    "auto3":{
                "marka":"Fiat",
                "model":"Freemont",
                "rok":2016,
                "kolor":["biały","srebrny"]
    }
}

print(autokomis)
print(autokomis["auto1"])
print(autokomis["auto1"]["marka"])
i=1
for a in autokomis.values():
    print("_______________________________")
    print("auto nr",i)
    for x,y in a.items():
        print(x," - ",y)
    i+=1
