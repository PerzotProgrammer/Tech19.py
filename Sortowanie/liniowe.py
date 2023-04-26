from random import randint

zakres = 1000
T = [randint(1, zakres) for i in range(10000)]

L = [0] * (zakres + 1)
for i in range(len(T)):
    L[T[i]] += 1

x = 0
for i in range(len(L)):
    if L[i] > 0:
        for j in range(L[i]):
            T[x] = i
            x += 1

print(T)