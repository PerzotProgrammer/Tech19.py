from random import randint

T = [randint(1, 1000) for i in range(10000)]

for i in range(len(T)):
    Tmin = i
    for j in range(i,len(T)):
        if T[j] < T[Tmin]:
            Tmin = j
    T[i], T[Tmin] = T[Tmin], T[i]

print(T)