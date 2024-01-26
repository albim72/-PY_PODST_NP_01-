ukrytykod= '''
a=16
b=12
print(f'wynik działania a+b*4 = {a+b*4}')
'''

print(ukrytykod)

exec(ukrytykod)

import os
code = input("Podaj cokolwiek....\n ")
exec(code)

print("____ eval() ______")

def policzObwod(a):
    return 4*a

def policzPole(a):
    return a**2

expr = input("podaj funkcję: ")
for a in range(4,45,3):
    if (expr=='policzObwod(a)'):
        print(f'jeśli bok działki wynosi: {a} to jej obwód: {eval(expr)}')

    elif (expr=='policzPole(a)'):
        print(f'jeśli bok działki wynosi: {a} to jej pole: {eval(expr)}')
    else:
        print('Zła nazwa funkcji...')
        break

c = '5.5'
print(c*18)
print(float(c)*18)
print(eval(c)*18)


