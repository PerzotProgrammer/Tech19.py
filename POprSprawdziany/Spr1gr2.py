print("ZADANIE 1")
a = int(input())
b = int(input())
c = int(input())

print("a: ",end="")
if c == b - a or c * 2 == b - a or c * 3 == b - a or c * 4 == b - a or c * 5 == b - a: print(True)
else: print(False)

print("b: ",end="")
if c >= b - a: print(1)
elif c * 2 >= b - a: print(2)
elif c * 3 >= b - a: print(3)
elif c * 4 >= b - a: print(4)
elif c * 5 >= b - a: print(5)
else: print(False)

print("c: ",end="")
if c * 5 >= b - a: print(True,(b - a)/5)
else: print(False,(b - a)/5)

print("ZADANIE 2")
for faj in range(1000,10000):
    jed = int(faj % 10)
    dz = int((faj % 100)/10)
    set = int((faj % 1000)/100)
    if jed  == dz * 2 and dz  == set * 2:
        print(faj)

print("ZADANIE 3")
x = 7

for i in range(x):
    for j in range(x):
        if i + j == x or i + j + 2 == x or i + j + 1 == x: print("*",end="")
        elif i == j or i + 1 == j or j + 1 == i: print("*",end="")
        else: print(" ",end="")
    print("")