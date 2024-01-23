#przykład 1
def witaj():
    print("witaj użytkowniku")
    print("witaj w naszej aplikacji...")
    print("zaloguj się!")


witaj()
p = witaj()
# p
print(type(p))

print("___________________________________________________")
#uruchom 20 razy (iteracyjnie) funkcję witaj()
for i in range(20):
    print("uruchomienie nr",i+1)
    witaj()

#przykład 2
def klient(nrtelefonu:int,kraj:str="Polska") -> str:
    return "Pochodzę z kraju: " + kraj + ", numer telefonu: " + str(nrtelefonu)

print("_______________________________________")
print(klient(43242343,"Niemcy"))
print(klient(54654655,"Włochy"))
print(klient(798677567))
print(klient('8769455895'))

#przykład 3

g = 10
def obliczenie(a,b,c):
    f = (a+b)*c-a*b
    f=2*f + g
    return f

print(obliczenie(4,7,4))
print(obliczenie(5.74,2,0))
print(obliczenie(-0.0005434,True,700))
# print(obliczenie('fsdf',True,700))

#przykład 4
def miasta(miasto1,miasto2="Radom",miasto3="Poznań"):
    print('konkurs na miasto tygodnia -> 1: ' + miasto1 + ", 2: " + miasto2 + ", 3: " + miasto3)

miasta("Tarnów","Bydogoszcz","Szczecin")
miasta("Tarnów","Bydogoszcz")
miasta("Tarnów")
miasta("Zamość",miasto3="Gdańsk")
miasta(miasto2="Puławy",miasto1="Wrocław",miasto3="Koszalin")

#przykład 5
def zamki(id,*zamek):
    print("id konkursu: " + str(id))
    print("zamek tygodnia -> 1: " + zamek[0] + ", 2: " + zamek[1] + ". 3: " + zamek[2])

zamki(23,"Malbork","Ogrodzieniec","Janowiec")
zamki(78,"Czersk","Malbork","Kazimierz Dolny","Ogrodzieniec","Janowiec","Będzin")


