a=100
b=1

if a>b:
    print("a jest wększe od b")
elif a == 1:
    print("a reprezentuje wartość 1")
elif a == b:
    print("a jest równe b")
else:
    print("a jest mniejsze niż b")


match a:
    case 1:
        print("a reprezentuje wartość 1")
    case 10:
        print("a reprezentuje wartość 10")
    case _:
        print("a jest inne niż 1 lub 10")

#rodzaje pętli

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
else:
    print("i nigdy nie osiągnie wartości 6")

owoce = ["jabłko","gruszka","banan","kiwi","czereśnia"]

print("________________________________")
for owoc in owoce:
    print(owoc)

print("________________________________")

cechy = ["kolorowy","elegancki","brudy","kosztowny","niechlujny"]
obiekty = ["budynek","płaszcz","ogród","samochód","przystanek"]

for x in cechy:
    for y in obiekty:
        print(x,y)
