print("ZADANIE 1")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print("a: ",int((a+b+c+d)/4))

print("b: ",end="")
if d - 2 <= a <= d + 2: print(True)
else: print(False)

print("c: ",end="")
temp = 0
if a < b: temp += 1
if b < c: temp += 1
if c < d: temp += 1
print(temp)

print("ZADANIE 2")
spr = 0

for col in range(10,100):
    temp = col

    for spr in range(0,10):
        if temp % 2 == 0:
            temp /= 2
        else:
            temp = (temp * 3)+1

    if temp == 1 and spr == 9:
        print(f"1 na 9 miejscu pojawia się w n = {col}")

print("ZADANIE 3")
x = 7

for i in range(x):
    for j in range(x):
        if i == int(x/2) or j == int(x/2): print("*",end="")
        elif j == i or i + j == x - 1: print("#",end="")
        else: print(" ",end="")
    print("")