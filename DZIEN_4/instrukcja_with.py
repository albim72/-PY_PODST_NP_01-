#instrukcja with

with open("dane.txt","r",encoding="utf-8") as f:
    dane = f.read()
    print(dane)

with open("abc.txt","w",encoding="utf-8") as f:
    f.write("abcd")

with open("abc.txt","w",encoding="utf-8") as f:
    f.write("yuytiuert")

with open("abc.dat","w",encoding="utf-8") as f:
    f.write("1,53,6,24,6,85,35")

#zapis do pliku binarnego

dane_binarne = b'to dane binarne: 32453646'

with open('binarny.bin','wb') as pb:
    pb.write(dane_binarne)




