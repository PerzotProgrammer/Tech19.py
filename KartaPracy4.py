#TODO zad1

#zad2


def dodaj(x,y):
    return x+y

#zad3
def silnia(x):
    if x == 0 : return 1
    else : return x * silnia(x-1)

#zad4
def fib(x):
    if x == 1 or x == 2 : return 1
    else : return fib(x-1) + fib(x-2)

#TODO zad5

#zad6
def po(x,y):
    if y == 0 : return 1
    if y == 1 : return x
    else : return x * po(x,y-1)

#zad7
from math import floor

def binar(x,numb = []):
    if x == 1 : 
        numb.append(1)
        return numb[::-1]
    else : 
        zeroJeden = x % 2
        numb.append(zeroJeden)
        x = floor(x/2)
        return binar(x)


#ROZWIĄZANIA
print("ZADANIE 2")
a = int(input("Liczba1: "))
b = int(input("Liczba2: "))
print("Wynik:",dodaj(a,b))

print("ZADANIE 3")
a = int(input("Silnia z: "))
print("Wynik:",silnia(a))

print("ZADANIE 4")
a = int(input("Który fib?: "))
print(a,"liczba w ciągu to",fib(a))

print("ZADANIE 6")
a = int(input("Podstawa: "))
a = int(input("Wykładnik: "))
print("Wynik to:",po(a,b))

print("ZADANIE 7")
a = int(input("Podaj liczbę na binarke: "))
print(f"Liczba {a} w binarnym to: {binar(a)}")