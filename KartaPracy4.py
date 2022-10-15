#zad1
def parzytstosc(x):
    if x % 2 == 0: return True
    else: return False

def netto(x):
    return x/1.23

def pelnoletnosc(x):
    if x >= 18 : return True
    else : return False

def mtf(x,p):
    if (x ** p - x) % p == 0 : return True
    else : return False

def dzielniki(x):
    for i in range (0,x) : 
        if x % i == 0 : print(i)

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

#TODO zad5 w rekurencji
def fib2(x,a=1,b=1):
    if x == 1 : return 1
    else:
        print(1)
        print(1)
        for i in range(x-2):
            a, b = b, a + b
            print(b)
             
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
        x = x//2
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

print("ZADANIE 5")
a = int(input("Ile fibów?: "))
fib2(a)

print("ZADANIE 6")
a = int(input("Podstawa: "))
a = int(input("Wykładnik: "))
print("Wynik to:",po(a,b))

print("ZADANIE 7")
a = int(input("Podaj liczbę na binarke: "))
print(f"Liczba {a} w binarnym to: {binar(a)}")