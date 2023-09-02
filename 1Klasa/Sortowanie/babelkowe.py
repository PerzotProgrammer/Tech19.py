from random import randint

T = [randint(1, 1000) for i in range(10000)]

for i in range(len(T) - 1):
    for j in range(0, len(T) - i - 1):
        if T[j] > T[j + 1]:
            T[j], T[j + 1] = T[j + 1], T[j]

print(T)