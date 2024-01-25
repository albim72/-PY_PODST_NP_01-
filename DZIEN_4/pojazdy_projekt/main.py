from samochod import Samochod
from motocykl import Motocykl

s1 = Samochod("Dodge","Journey","benzynowy",2018,899)
m1 = Motocykl("Harley Davidson","FXSB Breakout","benzynowy",2014,"chopper")

print("____ Samochód s1 ______")
print(s1)
jed = 54.3
odl = 612
cena_l = 6.48
print(f'spalanie [l/100km]: {s1.spalanie(odl,jed):.2f}')
print(f'koszt przejazdu na trasie {odl} km wynosi: {s1.koszt_przejazdu(odl,jed,cena_l):.2f} zł')

print("____ Motocykl m1 ______")
print(m1)
jed = 34.5
odl = 568
cena_l = 6.35
print(f'spalanie [l/100km]: {m1.spalanie(odl,jed):.2f}')
print(f'koszt przejazdu na trasie {odl} km wynosi: {m1.koszt_przejazdu(odl,jed,cena_l):.2f} zł')
