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
