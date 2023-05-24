# zad 3
suma = 0
for i in range(100, 1000):
    if i % 2 == 0:
        suma += i

print("Zad3:",suma)

# zad 4
ile = 0
for i in range(10,100):
    if i % 2 == 0 and i % 13 == 0:
        ile += 1

print("Zad4",ile)

# zad 5
liczba = int(input("Daj liczbe:"))
dzielniki = 0
for i in range(1,liczba + 1):
    if liczba % i == 0:
        dzielniki += i

print("Zad5",dzielniki)

# zad 6
liczba = int(input("Daj liczbe:"))
dzielniki = 0
for i in range(1,liczba):
    if liczba % i == 0:
        dzielniki += i

if dzielniki > liczba:
    print("Zad6","nie dzielniko-ujemna")
else:
    print("Zad6","dzielniko-ujemna")

# zad 7
from math import gcd, lcm
goraA = int(input("goraA:"))
dolA = int(input("dolA:"))
goraB = int(input("goraB:"))
dolB = int(input("dolB:"))

nww = lcm(dolA,dolB)

w1 = (nww // dolA) * goraA
w2 = (nww // dolB) * goraB

wynik = w1 + w2
nwd = gcd(wynik,nww)

print("Zad7",w1,"/",nww,"+",w2,"/",nww,"=",wynik,"/",nww)
print("Nieskracalna:",wynik/nwd,"/",nww/nwd)

# zad 8
slowo = input("Daj slowo:")
ile = 0
for i in slowo:
    if ord(i) % 2 == 0:
        ile += 1

print("Zad8",ile)

# zad 9
slowa = ""
for i in range(3):
    slowa += input("Daj slowo:")

if len(slowa) > 20:
    print("Zad9","więcej niż 20")
else:
    print("Zad9","mniej niż 20")
    