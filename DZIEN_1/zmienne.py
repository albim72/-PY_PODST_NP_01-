import math

a = "pora roku: zima"
b = 643
c = True

print(a,b,c,sep="---")
print(a+", "+str(b)+", "+str(c))

d = "następna pora roku: wiosna"
print("Pory roku -> " + a + ", " + d)

y = 11.6
print(8*y)
print(8+y)
print(8/y)
print(8-y)

g = "2.546435"
print(8*g)

print(8*float(g))

print(8*eval(g))

n1 = 11
n2 = 12

print(n1+n2, n1-n2, n1*n2, n1/n2, n1%n2)
# potęga liczby s

s = 10.51

print(s**2)
print(pow(5,2))

print(round(s))
print(math.sqrt(s))

print(s**0.5)
print(s**0.33333333)

#inkrementacja i dekrementacja
i=12
print(i+1)
print(i)
i+=1 #i=i+1
print(i)

i-=1
print(i)

i+=5
print(i)

#nie ma jawnego operatora inkrementacji ++

t = "lajkonik"

print(t)

#zmienne typu String są traktowane przez interpreter jak listy
print(t[0])
print(t[1])
print(t[2:6])
print(t[1:])
print(t[:4])
print(t[-1])
print(t[-2])
print(t[:len(t)-2])
print(t[-6:-2])
print(t[:67])
print(t[-14])
print(t[67])
