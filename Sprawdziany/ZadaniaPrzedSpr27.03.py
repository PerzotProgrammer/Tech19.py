# ZAGADNIENIA Napisy 
# - len, for, "foreach", ord, chr
# - indeksy, zakresy
# - konwersje list <-> napis
# - list - sort reverse
# - split, join
# Algorytmy - anagram, palindom, Boyer-Moore

# Wszystkie zadania wykonujemy na 26-znakowym
# alfabecie maturalnym: od A (65) do Z (90)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Przykładowe zadania:

# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis

# 5. Policz ile we wpisanym napisie jest liter A.

# 6. Podaj dominującą literkę we wpisanym napisie. 
# Niech to będzie tylko jedna literka.

# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"

# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)

# 10. Wypisz literki, których nie ma w napisie

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)


# PRE
napis = input("Daj ciąg: ")

# zad1
print(f"Pierwszy element: {napis[0]}\nDrugi element: {napis[len(napis) - 1]}")

print()

# zad2
for i in range(len(napis)):
    if i == 0:
        pass
    elif i == len(napis) - 1:
        break
    else: print(napis[i],end="")

print()

# zad3
print(napis[-1:-5:-1])

print()

# zad4
waga = 0
for i in range(len(napis) - 1):
    waga += ord(napis[i])

print(waga)

print()

# zad5
ileA = 0
for i in range(len(napis) - 1):
    if napis[i] == "a" or napis[i] == "A":
        ileA += 1

print(ileA)

print()

# zad6
maxNap = 0
for i in napis:
    spr = napis.count(i)
    if spr > maxNap:
        maxNap = spr
        literka = i
print(f"Dominandą jest {literka}, występuje ona {maxNap} razy!")

# zad7 

# Tu coś było ale nie działało

# zad8
ileLA = 0
for i in range(len(napis)):
    if napis[i] == "l" and napis[i + 1] == "a":
        ileLA += 1

print(f"LA występuje {ileLA} razy!")

print()

# zad9

# Nie ma drogi

# zad 10
listaLiter = napis.upper()
listaLiter = list(listaLiter)
listaLiter.sort()

ASCII = []
for i in range(65,91):
    ASCII.append(chr(i))

for i in ASCII:
    if i not in listaLiter:
        print(i,end=", ")

print()
print()