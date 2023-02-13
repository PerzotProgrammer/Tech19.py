# Zad 1

a = int(input())
b = int(input())
da = []
db = []

for i in range(1,a):
    if a % i == 0:
        da.append(i)

for i in range(1,b):
    if b % i == 0:
        db.append(i)

suma = sum(da)
sumb = sum(db)

print(suma,sumb)

if suma == b + 1 and sumb == a + 1: print(True)
else: print(False)

