# NWW Z NWD Euklidesem
print("ZADANIE 1")
a = int(input("Podaj 1 liczbę: "))
b = int(input("Podaj 2 liczbę: "))

temp = a * b

while a != b :
    if a > b :
        a -= b
    else :
        b -= a

NWD = a

NWW = temp // NWD # WAŻNY WZÓR!!!

print(f"NWD = {NWD} , NWW = {NWW}")


# NWW z NWD Modulo
print("ZADANIE 2")
a = int(input("Podaj 1 liczbę: "))
b = int(input("Podaj 2 liczbę: "))

temp = a * b

while b > 0 :
    mod = a % b
    a = b
    b = mod

NWD = a

NWW = temp // NWD

print(f"NWD = {NWD} , NWW = {NWW}")
