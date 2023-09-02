# Program dodający dwa ułamki

a = int(input())
b = int(input())
c = int(input())
d = int(input())

A = a
B = b
C = c
D = d

temp = b * d

while b != d :
    if b > d :
        b -= d
    else :
        d -= b

NWD = b
NWW = temp // NWD

w1 = (NWW // B) * A
w2 = (NWW // D) * C

print(f"{A}/{B} + {C}/{D} = {w1 + w2}/{NWW}")