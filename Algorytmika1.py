#1.Algorytm czy liczba pierwsza
x = int(input("Podaj liczbę: "))
temp = 0
for i in range(1,x+1):
    if x % i == 0:
        temp += 1
if temp == 2: print(True)
else: print(False)

#2.Pętla wyznaczająca liczby pierwsze w przedziale (a,b)
a = int(input("Podaj start: "))
b = int(input("Podaj stop: "))
for x in range(a, b):
    temp = 0
    for i in range(1,x+1):
        if x % i == 0:
            temp += 1
    if temp == 2: print(x)