#zad1
print("ZADANIE 1")
a = int(input("Liczba1: "))
b = int(input("Liczba2: "))
if (a + b) % 2 == 0: print("TAK, parzysta")
else: print("NIE, nie parzysta")

#zad2
print("ZADANIE 2")
from math import sqrt
a = float(input("Liczba1: "))
b = float(input("Liczba2: "))
if (a + b) / 2 > sqrt(a * b) : print("TAK, średnia ary. > geo.")
else : print("NIE, średnia ary. < geo.")

#zad3
print("ZADANIE 3")
a = int(input("Liczba1: "))
b = int(input("Liczba2: "))
c = int(input("Liczba3: "))
if a == b or a == c or b == c : 
    print("TAK, przynajmniej dwie są równe")
    if a == b and a == c and b == c : print("Wszystkie liczby są równe")
    elif a == b : print("są to: 'Liczba1' i 'Liczba2'")
    elif a == c : print("są to: 'Liczba1' i 'Liczba3'")
    elif b == c : print("są to: 'Liczba2' i 'Liczba3'")
else : print("NIE, nie ma równych")

#zad4
print("ZADANIE 4")
a = int(input("Liczba1: "))
b = int(input("Liczba2: "))
c = int(input("Liczba3: "))
d = int(input("Liczba4: "))
if a < b and a < c and a < d: print("Najmniejsza liczba to ",a)
elif b < a and b < c and b < d : print("Najmniejsza liczba to ",b)
elif c < a and c < b and c < d : print("Najmniejsza liczba to ",c)
elif d < a and d < b and d < c : print("Najmniejsza liczba to ",d)
else : print("Są dwie najmniejsze liczby równe siebie!")

#zad5
print("ZADANIE 5")
a = int(input("Liczba1: "))
b = int(input("Liczba2: "))
c = int(input("Liczba3: "))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b : print("TAK, spełnia nierówność")
else : print("NIE, nie spełnia nierówności")

#zad6
print("ZADANIE 6")
a = int(input("Liczba1: "))
b = int(input("Liczba2: "))
c = int(input("Liczba3: "))
if a < b + c and b < a + c and c < a + b : 
    print("Trójkąt powstanie")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 : print("Będzie to trójkąt prostokątny")
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2 : print("Będzie to trójkąt rozwartokątny")
    elif a**2 + b**2 > c**2 or b**2 + c**2 > a**2 or c**2 + a**2 > b**2 : print("Będzie to trójkąt ostrokątny")
else : print("Trójkąt nie powstanie")