#zad1

# MOŻNA TO ZROBIĆ ZA POMOCĄ
# from calendar import month
#print(month(2022,11))

print("ZADANIE 1")
print("\t\tLISTOPAD 2022")
print("Pn\tWt\tŚr\tCw\tPt\tSo\tNd")
j = 1
print("\t",end="")
for i in range(1,31):
    print(i, end="\t")
    j += 1
    if j == 7:
        print()
        j = 0
print()

#zad2
print("ZADANIE 2")
ileLiczb = int(input("Podaj zakres potęg: "))
for i in range(1,ileLiczb):
    if i % 2 != 0:
        print(f"{i}^2={i**2}")

#zad3
print("ZADANIE 3")
for i in range(1000,10000):
    if i % 379 == 0:
        print(i)

#zad4
print("ZADANIE 4")
for i in range(100,1000):
    if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
        print(i)

#zad5
print("ZADANIE 5")
ileLiczb = int(input("Ile liczb chcesz wpisać?: "))
Liczby = []
for i in range(0,ileLiczb):
    temp = int(input(f"Podaj {i+1} liczbę: "))
    Liczby.append(temp)
print(f"Wynik to: {sum(Liczby)}")

#zad6
print("ZADANIE 6")
ileLiczb = int(input("Podaj liczby: "))
suma = 0
for i in range(2,(ileLiczb*2)+2,+2):
    suma += i
print(f"Suma to: {suma}")

#zad7
print("ZADANIE 7")
ileLiczb = int(input("Podaj liczby: "))
suma = 0
for i in range(11,(ileLiczb*2)+11,+2):
    suma += i
print(f"Suma to: {suma}")

#zad8
print("ZADANIE 8")
kapPocz = int(input("Podaj początkową wartość inwestycji: "))
lataInw = int(input("Podaj lata inwestycji: "))
kapKon = 0
suma = kapPocz
for i in range(0,lataInw * 12):
    kapKon = suma * 0.06 * (1/12)
    suma += kapKon
print(f"Końcowy kapitał wynosi: {round(suma,2)} zł")

#zad9
print("ZADANIE 9")
ileLiczb = int(input("Podaj ilość liczb: "))
j = 21
suma = 0
for i in range(0,ileLiczb+1):
    for a in range(0,i,j):
        print(j)
        suma += j
        j += 100
print(f"Suma to: {suma}")

#zad10
from cmath import sqrt
print("ZADANIE 10")
for i in range(1,1000):
    if i - (i//10)*10 == sqrt(i):
        print(i)
    elif i - (i//100)*100 == sqrt(i):
        print(i)
    