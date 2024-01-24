def kwota(t,nw,w,u,i,rab=0):
    if rab>=0 and rab <= 70:
        return (nw+t)*(1-rab/100)+w+u+i
    else:
        return "podaj rabat z przedziału 1% - 70%"

print("kwota do zapłaty:",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty:",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty:",kwota(100,100,50,50,50,75),"zł")

#Tworzenie listy z dostępnymi opcjami rabatu (wartości dyskretne)
rabs = [0,8,10,12,15,20,22,25,35,50]

wynik = []
for r in rabs:
    kw = kwota (1700, 1230, 450, 200, 180, r)

    if r == 0:
        print ("cena bazowa do zapłaty wynosi:",kw,"zł")

    else:
        print ("dla rabatu:", r, "%, kwota do zapłaty wynosi:", kw,"zł")

    wynik.append(kw)


print (wynik)

result = [kwota(1700,1230,450,200,180,r) for r in rabs]
print(result)

