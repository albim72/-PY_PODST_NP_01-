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
