import os

f = open("danex.txt","r",encoding="utf-8")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()
print("_"*50)
# print(f.readline())

f = open("danex.txt","r",encoding="utf-8")
print(f.read())
f.close()
print("_"*50)
f = open("danex.txt","r",encoding="utf-8")
for i in f:
    print(i)

f.close()

print("__________ zapis do pliku - w __________")

f = open("message.txt","w",encoding="utf-8")
f.write("to jest pierwsza linia\n")
f.close()

print("__________ zapis do pliku - a __________")
f = open("info.txt","a",encoding="utf-8")
f.write("to jest n-ta linia\n")
f.close()

# print("__________ zapis do pliku - b __________")
# f = open("bane.txt","bw")
# f.write()
# f.close()

print("wyświetlenie informacji z pliku info.txt")

f = open("info.txt","r",encoding="utf-8")
print(f.read())
f.close()

if os.path.exists("info.txt"):
    os.remove("info.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje!")

