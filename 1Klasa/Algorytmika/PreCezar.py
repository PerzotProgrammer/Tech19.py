# PRE

# Funkcja ord() - zwraca kod ascii dla znaku
x = input()
print("wynik ord:",ord(x))

# Funkcja chr() - zwraca znak dla kodu ascii
x = int(input())
print("wynik chr:",chr(x))

# ZAD1 napisz alfabet za pomocą znaków
print("ZADANIE 1")
litera = ord("A")
x = 0
for i in range(0,26):
    print(chr(litera), end=" ")
    litera += 1

# ZAD2 napisz pętle wyciągającą litery z napisu
print("ZADANIE 2")
napis = input()
for i in range(len(napis)):
    print(napis[i])

# ZAD3 napisz pętle wyciągającą kody ascii z napisu
print("ZADANIE 3")
napis = input()
for i in range(len(napis)):
    print(ord(napis[i]))