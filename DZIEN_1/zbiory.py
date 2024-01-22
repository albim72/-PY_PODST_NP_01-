drzewa = {"buk","dąb","jesion","baobab","jabłoń","tuja","dąb"}
print(drzewa)
print(drzewa)
print(drzewa)

print(type(drzewa))

print("jesion" in drzewa)
print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)

drzewa.update(["topola","wierzba"])
print(drzewa)

drzewa.remove("osika")
print(drzewa)

drzewa.discard("heban")
print(drzewa)

drzewa.discard("dąb")
print(drzewa)

