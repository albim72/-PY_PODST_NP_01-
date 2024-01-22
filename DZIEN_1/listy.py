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
