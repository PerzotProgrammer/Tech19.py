# 1. NWD na Euklidesie
print("ZADANIE 1")
a = int(input("Podaj 1 liczbę: "))
b = int(input("Podaj 2 liczbę: "))

while a != b :
    if a > b :
        a -= b
    else :
        b -= a

print(f"NWD = {a}")


# 2. NWD na modulo bo Pan Nowak kazał
print("ZADANIE 2")
a = int(input("Podaj 1 liczbę: "))
b = int(input("Podaj 2 liczbę: "))
temp = 0

while b != 0 :
    temp = a % b
    a = b
    b = temp

print(f"NWD = {a}")





