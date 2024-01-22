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
