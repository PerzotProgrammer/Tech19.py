# zadanko 1
print("ZAD 1")

def nwd(x,y):
    while x != y:
        if x > y: x -= y
        else: y -= x
    return x

def nww(x,y):
    temp = x * y
    return temp // nwd(x,y)

def nww3(x,y,z):
    return nww(x,nww(y,z))

ax = int(input())
print("---")
ay = int(input())
print()
bx = int(input())
print("---")
by = int(input())
print()
cx = int(input())
print("---")
cy = int(input())
print()

mian = nww3(ay, by, cy)

ax *= (mian // ay)
bx *= (mian // by)
cx *= (mian // cy)

print(f"Wspólny mianownik to: {mian}")
print(f"{ax}/{mian}, {bx}/{mian}, {cx}/{mian}")


# Zadanko 2
print("ZAD 2")

def SumaDzielnikow(x):
    suma = 0
    for i in range(1,x):
        if x % i == 0:
            suma += i
    return suma

T = []
for i in range(1,5000):
    spr1 = SumaDzielnikow(i)
    T.append(spr1)
    spr2 = SumaDzielnikow(spr1)
    if i == spr2 and spr1 != spr2 and spr2 not in T:
        print(f"Znaleziono!:{spr1,spr2}")


# Zadanko 3
print("ZAD 3")

def CzyPierwsza(x):
    dzielnik = 0
    for i in range(1,x + 1):
        if x % i == 0:
            dzielnik += 1
    if dzielnik == 2:
        return True
    else: return False

for liczba in range(2,500):
    Lp = []
    for spr in range(1,liczba + 1):
        if liczba % spr == 0 and CzyPierwsza(spr):
            Lp.append(spr)
    if len(Lp) == 3:
        wynik = 1
        for i in Lp:
            wynik *= i
        if wynik == liczba:
            print(f"Znaleziono!:{liczba}")

