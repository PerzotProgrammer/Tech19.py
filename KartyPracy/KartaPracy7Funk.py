import random, numpy as np
# PRE (generacja tablicy)
ileLiczb = 40
T = []
for i in range(ileLiczb):
    T.append(random.randint(10, 100))

print(f"Twoja tablica T posiada następujące liczby:\n{T}")

# ZAD 1
print(f"Maksymalna wartość to: {max(T)}")

# ZAD 2
print(f"Minimalna wartość to: {min(T)}")

# ZAD 3
print(f"Rozpiętość tablicy to: {len(T)}")

# ZAD 4
Tsorted = sorted(T)
Tsorted.reverse()
for i in range(len(Tsorted)):
    if max(Tsorted) > Tsorted[i]:
        print(f"Vice-maksymalna wartość to: {Tsorted[i]}")
        break

# ZAD 5
Tsorted.reverse()
for i in range(len(Tsorted)):
    if min(Tsorted) < Tsorted[i]:
        print(f"Vice-minimalna wartość to: {Tsorted[i]}")
        break

# ZAD 6
print(f"Ilość maksów to: {T.count(max(T))}")

# ZAD 7
print(f"Ilość minów to: {T.count(min(T))}")

# ZAD 8
wybor = int(input("Podaj szukaną wartość: "))

if T.count(wybor) > 0:
    print(f"W tablicy znajduje się {T.count(wybor)} takich liczb!")
else:
    print("W tablicy nie ma takiej liczby!")

# ZAD 9

print(f"Średnia elementów to: {round(np.average(T), 1)} (dokładność do 1 miejsca)")

# ZAD 10 
sumaP = 0
for i in range(len(T)):
    if i % 2 == 0:
        sumaP += T[i]

print(f"Suma parzystych indeksów to: {sumaP}")

# ZAD 11
sredniaNP = []
for i in range(len(T)):
    if i % 2 != 0:
        sredniaNP.append(T[i])


print(f"Średnia elementów pod nieparzystymi indeksami to: {round(np.average(sredniaNP), 1)} (dokładność do 1 miejsca)")

# ZAD 12
TniePow = set(T)
TniePow = list(TniePow)
print(f"Nie powtarzające się elementy to: {TniePow}")