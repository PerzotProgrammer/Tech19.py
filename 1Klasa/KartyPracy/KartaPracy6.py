print("ZADANIE 1")

input1 = int(input())
input2 = int(input())
input3 = int(input())

print("ARYTMETYCZNY:")
if input1 - input2 == input2 - input3: print(True)
else : print(False)

print("GEOMETRYCZNY:")
if input2 / input1 == input3 / input2: print(True)
else : print(False)


print("ROSNĄCY:")
if input1 < input2 and input2 < input3: print(True)
else : print(False)


print("MALEJĄCY:")
if input1 > input2 and input2 > input3: print(True)
else : print(False)


print("ZADANIE 2")
suma = 0
liczba = 0
for i in range(100, 1000):
    if i % 8 == 0 and i % 16 != 0:
        suma += i
print(f"Wynik to: {suma}")


print("ZADANIE 3")
for i in range(10, 100):
    if i % 7 == 0:
        dzielnik = i
for i in range(1000, 10000):
    if i % dzielnik == 0:
        liczba += i
print(f"Wynik to: {liczba}")


print("ZADANIE 4")
ilosc = 0
for i in range(10,100):
    jed = i % 10
    dz = i / 10
    if jed * 2 <= dz:
        ilosc += 1
print(ilosc)


print("ZADANIE 5")
ilosc = 0
suma = 0
for i in range(100,1000):
    jed = i % 10
    dz = (i % 100) / 10
    set = (i % 1000) / 100
    if set > jed + dz:
        ilosc += 1
        suma += i
print(f"Ilość: {ilosc}\nSuma: {suma}")


print("ZADANIE 6")
input1 = int(input())
licznik = 0
suma = 0
for i in range(10,100):

    if i % 19 == 0:
        licznik += 1
        suma += i
    if licznik == input1:
        print(suma)
        break
    if i == 99:
        print("OUT OF RANGE!")


print("ZADANIE 7")
input1 = int(input())
licznik = 0
suma = 0
for i in range(999,99,-1):
    if i % 37 == 0:
        licznik += 1
        suma += i
    if licznik == input1:
        print(suma)
        break
    if i == 100:
        print("OUT OF RANGE!")


