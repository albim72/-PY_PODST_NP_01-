import copy

oryginalny_obiekt = {
    'a':1,
    'b':[2,3,{'c':4,'d':[5,6]}]
}

sobiekt = oryginalny_obiekt.copy()
print(sobiekt)

kobiekt = copy.deepcopy(oryginalny_obiekt)
print(kobiekt)

oryginalny_obiekt['b'][2]['c'] = 99

print(oryginalny_obiekt)
print(sobiekt)
print(kobiekt)
