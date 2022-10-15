#TODO zad1

#zad2
def SumaCyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //=10
    
    return suma

# print(SumaCyfr(pow(2,2019)))

#TODO zad3


#zad4
def Dzielnik(x,y):
    if x % y == 0: return True
    else: return False

#zad5 to zad2?

#TODO zad6


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