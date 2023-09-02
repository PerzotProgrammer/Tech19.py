import random
# PRE (generacja tablicy)
ileLiczb = 40
T = []
for i in range(ileLiczb):
    T.append(random.randint(10, 100))

print(f"Twoja tablica T posiada następujące liczby:\n{T}")

# ZAD 1
Tmax = T[0]
for i in range(len(T)):
    if T[i] > Tmax:
        Tmax = T[i]

print(f"Maksymalna wartość to: {Tmax}")

# ZAD 2
Tmin = T[0]
for i in range(len(T)):
    if T[i] < Tmin:
        Tmin = T[i]

print(f"Minimalna wartość to: {Tmin}")

# ZAD 3
print(f"Rozpiętość tablicy to: {len(T)}")

# ZAD 4
TviceMax = T[0]
for i in range(len(T)):
    if T[i] > TviceMax and T[i] < Tmax:
        TviceMax = T[i]

print(f"Vice-maksymalna wartość to: {TviceMax}")

# ZAD 5
TviceMin = T[0]
for i in range(len(T)):
    if T[i] < TviceMin and T[i] > Tmin:
        TviceMin = T[i]

print(f"Vice-minimalna wartość to: {TviceMin}")

# ZAD 6
TileMax = 0
for i in range(len(T)):
    if T[i] == Tmax:
        TileMax += 1

print(f"Ilość maksów to: {TileMax}")

# ZAD 7
TileMin = 0
for i in range(len(T)):
    if T[i] == Tmin:
        TileMin += 1

print(f"Ilość minów to: {TileMin}")

# ZAD 8
wybor = int(input("Podaj szukaną wartość: "))
iloscWyboru = 0
for i in range(len(T)):
    if wybor == T[i]:
        iloscWyboru += 1

if iloscWyboru > 0:
    print(f"W tablicy znajduje się {iloscWyboru} takich liczb!")
else:
    print("W tablicy nie ma takiej liczby!")

# ZAD 9
srednia = 0
for i in range(len(T)):
    srednia += T[i]
srednia /= len(T)
srednia = round(srednia, 1)

print(f"Średnia elementów to: {srednia} (dokładność do 1 miejsca)")

# ZAD 10
sumaP = 0
for i in range(len(T)):
    if i % 2 == 0:
        sumaP += T[i]

print(f"Suma parzystych indeksów to: {sumaP}")

# ZAD 11
sredniaNP = 0
iloscNP = 0
for i in range(len(T)):
    if i % 2 != 0:
        sredniaNP += T[i]
        iloscNP += 1
sredniaNP /= iloscNP
sredniaNP = round(sredniaNP,1)

print(f"Średnia elementów pod nieparzystymi indeksami to: {sredniaNP} (dokładność do 1 miejsca)")

# ZAD 12 i 14
TniePow = []
ileUsunac = 0
for i in range(len(T)):
    temp = T[i]
    licz = 0
    for j in range(len(T)):
        if temp == T[j]:
            licz += 1
            if licz >= 2:
                ileUsunac += 1
                break
    else:
        TniePow.append(temp)

print(f"Nie powtarzające się elementy to: {TniePow}")

# ZAD 13
notInT = []
for i in range(10,100):
    if i not in T:
        notInT.append(i)
print(f"Tablica nie posiada: {notInT}")

# ZAD 14 wypisz
print(f"Aby zostały wartości unikalne należy usunąć {ileUsunac} liczb")

# ZAD 15
najCiag = 0
Ciagi = [0] * len(T)
indeks = 0
flaga = 0
for i in range(len(T)):
    if T[i] >= T[i-1]:
        Ciagi[indeks] += 1
    else:
        flaga = 1
    if flaga == 1:
        indeks += 1
        flaga = 0

for i in range(len(Ciagi)):
    if Ciagi[i] > najCiag:
        najCiag = Ciagi[i]

print(f"Najwiękrzy niemalejący ciąg składa się z {najCiag} liczb")