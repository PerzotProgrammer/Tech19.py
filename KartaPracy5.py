#zad1
def sumaPierwszych():
    wynik = 0
    for liczba in range(10, 100):
        n = 0
        for dzielnik in range(2, liczba):
            if liczba % dzielnik == 0:
                n += 1
        if n == 0:
            wynik += liczba
    return wynik

#zad2
def SumaCyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //=10
    
    return suma

#TODO zad3


#zad4
def Dzielnik(x,y):
    if x % y == 0: return True
    else: return False

#zad5 to zad2?

#zad6.1
def pierwsza1(x):
    if x % 2 == 0: return druga1(x)
    else: return False

def druga1(x):
    x *= 3
    if x % 2 != 0: return trzecia1(x)
    else: return False

def trzecia1(x):
    return x * 0.4

#zad6.2
def pierwsza2(x):
    if x % 2 == 0: return x
    else: return False

def druga2(x):
    x *= 3
    if x % 2 != 0: return x
    else: return False

def trzecia2(x):
    return x * 0.4

# nie wiem czy o to chodzi w zad6

print("ZADANIE 1")
print("Suma dwucyfrowych liczb pierwszych to:",sumaPierwszych())

print("ZADANIE 2")
print(f"Suma cyfr liczby {pow(2,2019)} czyli 2^2019 to {SumaCyfr(pow(2,2019))}")

print("ZADANIE 4")
a = int(input("Liczba:"))
b = int(input("Dzielnik:"))
if Dzielnik(a,b) == True: print(f"TAK, {b} jest dzielnikiem {a}")
else : print(f"NIE, {b} nie jest dzielnikiem {a}")

print("ZADANIE 5")
a = int(input("Podaj liczbę aby dostać sumę cyfr: "))
print(f"Suma cyfr to: {SumaCyfr(a)}")

print("ZADANIE 6.1")
a = int(input("Liczba: "))
print(pierwsza1(a))

print("ZADANIE 6.2")
a = int(input("Liczba: "))
print(trzecia2(druga2(pierwsza2(a))))
