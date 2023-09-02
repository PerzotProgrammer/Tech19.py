print("ZADANIE 1")
x = int(input("Podaj liczbę: "))
wynik = 0

while x > 0:
    wynik += x % 10
    x //= 10

print(f"Wynik to: {wynik}")


print("ZADANIE 2")
x = int(input("Podaj liczbę: "))
spr = 0

for i in range(2,x):
    if x % i == 0:
        spr += 1

if spr == 0:
    print("Pierwsza")
else:
    print("Nie Pierwsza")


print("ZADANIE 3")
x = int(input("Podaj liczbę: "))
spr = 0

for i in range(1,x):
    if x % i == 0:
        spr += i

if spr == x:
    print("Doskonała")
else:
    print("Nie Doskonała")


print("ZADANIE 4")
x = int(input("Podaj liczbę: "))
y = int(input("Podaj liczbę: "))

while x != y:
    if x > y:
        x -= y
    else:
        y -= x

if x == 1:
    print("Liczby są względnie pierwsze")
else:
    print("Liczby nie są względnie pierwsze")


print("ZADANIE 5")
X = int(input("Podaj liczbę: "))
for Y in range(10,20):
    x = X
    y = Y
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    if x == 1:
        print(Y)


print("ZADANIE 6")
x = int(input("Liczebnik: "))
y = int(input("Mianownik: "))
X = x
Y = y
while x != y:
    if x > y:
        x -= y
    else:
        y -= x
X //= x
Y //= y
print(f"Ułamek to: {X}/{Y}")


print("ZADANIE 7")
x = int(input("Liczebnik: "))
y = int(input("Mianownik: "))
X = x
Y = y
while x != y:
    if x > y:
        x -= y
    else:
        y -= x
X //= x
Y //= y

if X >= Y:
    liczba = X // Y
    X -= Y * liczba
print(f"Liczba mieszana to: {liczba} i {X}/{Y}")



print("ZADANIE 8")
T = []
for i in range(2,100000):
    
    spr1 = 0
    for j in range(1,i):
        if i % j == 0:
            spr1 += j
    T.append(spr1)
    spr2 = 0
    for k in range(1,spr1):
        if spr1 % k == 0:
            spr2 += k

    if i == spr2 and spr1 != spr2 and spr2 not in T:
        print(f"({spr1},{spr2})")


#PRE 9
def Pierwsza(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


print("ZADANIE 9")
for i in range(1,100):
    for j in range(2,i):
        if i % j == 0:
            if Pierwsza(j) and Pierwsza(i//j):
                print(i)
                break


print("ZADANIE 10")
x = int(input("Podaj liczbę: "))
spr = 0
for i in range(2,x):
    if x % i == 0:
        spr += 1
if spr == 0:
    print("Jest to liczba pierwsza")
    spr = 0
    y = x + 2
    for j in range(2,y):
        if y % j == 0:
            spr += 1
    if spr == 0:
        print(f"Jej bliźniak to {y}!")
    else:
        spr = 0
        z = x - 2
        for k in range(2,z):
            if z % k == 0:
                spr += 1
        if spr == 0 and z != 0:
            print(f"Jej bliźniak to {z}!")
        else:
            print("Liczba nie ma bliźniaka")
else:
    print("Nie jest to liczba pierwsza!")