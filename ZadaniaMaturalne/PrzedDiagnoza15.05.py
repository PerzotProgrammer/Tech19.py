# WSTĘP

#zad 1
suma = 0
for i in range(100, 1000):
    suma += i
print(suma)

#zad 2
suma = 0
for i in range(10,100):
    if i % 6 == 0:
        suma += i
print(suma)

#zad 3
from random import randint
losowe = []
for i in range(5): losowe.append(randint(1000, 10000))
print(f"{losowe} max: {max(losowe)}")

#zad4
liczba = input("Daj liczbę:")
suma = 0
for i in liczba:
    suma += int(i)
print(f"Suma to: {suma}")

#zad 5
liczba = input("Daj liczbę:")
Tab = []
for i in liczba:
    Tab.append(int(i))
print(f"Minimalna to: {min(Tab)}")

# ALGO

#zad 1
def CzyPierwsza(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

liczba = int(input("Daj liczbe:"))
if CzyPierwsza(liczba):
    print("Tak, Pierwsza")
else:
    print("Nie, Niepierwsza")

#zad 2
def CzyZlozona(x):
    for i in range(2,x):
        if x % i == 0:
            return True
    return False

liczba = int(input("Daj liczbe:"))
if CzyZlozona(liczba):
    print("Tak, Złożona")
else:
    print("Nie, Niezłożona")

#zad 3
from math import gcd
liczba = int(input("Daj liczbe:"))
if gcd(liczba,24) == 1:
    print("Tak, Względnie pierwsza z 24")
else:
    print("Nie, Niewzględnie pierwsza z 24")

#zad 4
napis = input("Podaj napis do szyfracji: ")
szyfr = ""
klucz = int(input("Podaj klucz: "))

for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + klucz) % 26)
print("Szyfracja:", szyfr)

#zad 5 (nie do końca)
from math import lcm

goraA = int(input("GoraA:"))
dolA = int(input("DolA:"))
goraB = int(input("GoraB:"))
dolB = int(input("DolB:"))

nww = lcm(dolA, dolB)
w1 = (nww // dolA) * goraA
w2 = (nww // dolB) * goraB

goraW = w1 + w2
dolW = nww

print(f"{goraA}/{dolA} + {goraB}/{dolB} = {goraW}/{dolW}")
print(f"czyli: {(w1 + w2)/dolW}")


#zad 5

def nww(a, b):
    temp = a * b
    while a != b :
        if a > b :
            a -= b
        else :
            b -= a
    return temp // a

print(nww(24, 36))

# NAPISY

#zad 1

napis = input("Daj stringa: ")
ilosc = 0
for i in napis:
    if i == "C" or i == "c":
        ilosc += 1
print(f"W napisie znajduje się {ilosc} liter c")


#zad 2 (definicja rosnącości : a < z bo ord(a) < ord(z))

def CzyRosnacy(napis : str):
    for i in range(1,len(napis)):
        if ord(napis[i]) >= ord(napis[i - 1]):
            return True
    return False


napis = input("Daj stringa: ")

if not CzyRosnacy(napis):
    print("Napis jest nierosnący")
else:
    print("Napis jest rosnący")


#zad 3
stringi = []

for i in range(3):
    stringi.append(input("Daj stringa: "))

wynik = ""
for i in range(3):
    if len(stringi[i]) > len(wynik):
        wynik = stringi[i]
print(f"Najdłuższy napis to: {wynik}")