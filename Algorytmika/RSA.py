from math import gcd as NWD # Greatest Common Dividor - czyli NWD

# Dobór dwóch liczb pierwszych
pie1 = 11
pie2 = 13

# Trzowrzenie funkcji F = (pie1 - 1) * (pie2 - 1) i znalezienie N = pie1 * pie2
F = (pie1 - 1) * (pie2 - 1)
N = pie1 * pie2

# Znalezienie klucza publicznego E: NWD(F,E) = 1
for i in range(2, F):
    if NWD(i, F) == 1:
        E = i
        break
# print(E, N)

# Znalezienie klucza prywatnego D: D * E mod F = 1 (odwrotność modulo)
for i in range(2, N):
    if (i * E) % F == 1:
        D = i
        break
# print(D,N)

# PRZYKŁADY
# C = (x ** E) % N (Szyfrogram)
# T = (C ** D) % N (Na tekst jawny)

msg = input("Podaj słowo do szyfracji: ")

szyfr = ""
for i in msg:
    szyfr += chr((ord(i) ** E) % N)
print("Twój szyfr:", szyfr)

jawny = ""
for i in szyfr:
    jawny += chr((ord(i) ** D) % N)
print("Twoja deszyfracja:", jawny)
