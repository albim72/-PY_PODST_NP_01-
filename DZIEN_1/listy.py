kraje = ["Polska","Szwecja","Słowacja","Niemcy","Hiszpania","Irlandia"]
print(kraje)
print(type(kraje))
kraje.append("Włochy")
print(kraje)

kraje.insert(3,"Francja")
kraje.insert(2,"Niemcy")
print(kraje)

kraje.sort()
print(kraje)

liczby = [2,64,116,-45,0,7,8,128,90,-12,3,-6,101,116,2]

liczby.reverse()
print(liczby)

liczby.sort()
print(liczby)

liczby.sort(reverse=True)
print(liczby)

liczby.remove(-45)
print(liczby)

liczby.remove(116)
print(liczby)

poz = liczby.index(101)
print(poz)

del liczby[poz]

print(liczby)

sklepzoo = [[["Buldog angielski","Owczarek Podhalański","Wyżeł"],"kot","papuga","mysz"],[[7500,2500,5600],1200,900,45],[True,90,"Takietam",9.06]]
print(sklepzoo)

print(sklepzoo[0])
print(sklepzoo[0][1])
print(sklepzoo[0][0])
print(sklepzoo[0][0][0], "-",sklepzoo[1][0][0]," zł")

#konkatenacja tablic
miasta = ["Kielce","Radom","Lublin","Rzeszów"]
stolica = ["Warszawa","Rzym","Londyn"]

print(miasta)
print(stolica)

miasta = miasta + stolica

print(miasta)

m = miasta + ["Zamość","Koszalin"]

print(m)

miasta.remove("Radom")
print(miasta)
print(m)

#operacje na listach
litery = ['a','b','c','d','e','f','g','h','x','y','z']
print("przed zmianą: ", litery)
litery[2:7] = [98,53,23,56,78,34,101]
print("po zmianie: ", litery)

litery_x = litery
#nowe listy
litery_p = list(litery)
litery_q = litery[:]
litery_z = litery_p.copy()

print("litery_x przed zmianą: ", litery_x)
print("litery przed zmianą: ", litery)
print("litery_p przed zmianą: ", litery_p)
print("litery_q przed zmianą: ", litery_q)
print("litery_z przed zmianą: ", litery_z)

litery[:] = [1001,1002,1006,1010]
print("___________________________________")
print("litery_x po zmianie: ", litery_x)
print("litery po zmianie: ", litery)
print("litery_p po zmianie: ", litery_p)
print("litery_q po zmianie: ", litery_q)
print("litery_z po zmianie: ", litery_z)

print("__________________identyfikatory dla litery i litery_x _________________")
print(id(litery))
print(id(litery_x))
print(id(litery_p))
print(id(litery_q))
print(id(litery_z))

kolory = ["zielony","czerwony","niebieski","biały","czarny","złoty"]

parzysta = kolory[::2]
nieparzysta = kolory[1::2]
spec= kolory[0:5:3]

print(parzysta)
print(nieparzysta)
print(spec)

info = "tekst pisany normalnie"
print(info)
wspak = info[::-1]
print(wspak)

 
