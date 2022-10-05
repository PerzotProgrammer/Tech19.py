print("ZADANIE 1")
a = int(input("Liczba: "))
if a % 3 == 0: 
    print("TAK Liczba dzieli się przez 3")
else : 
    print("NIE Liczba nie dzieli się przez 3")


print("ZADANIE 2")
a = int(input("Liczba: "))
if a % 17 == 0 and 100 <= a < 1000: # lub len(str(a))
    print("TAK Liczba dzieli się przez 17 i jest 3 cyfrowa")
else : 
    print("NIE Liczba nie spełnia warunków")


print("ZADANIE 3")
a = int(input("Podaj wiek: "))
if a >= 18 :
    print("Pełnoletni")
else :
    print("Niepełnoletni")


print("ZADANIE 4")
limit = 20 #const? python nie ma stałych
a = int(input("Waga ciężarówki: "))
if a <= limit :
    print("Waga poniżej limitu")
else:
    print("Waga powyżej limitu")


print("ZADANIE 5")
a = int(input("Liczba 1: "))
b = int(input("Liczba 2: "))
c = int(input("Liczba 3: "))
if a < c < b or a > c > b :
    print("TAK")
else :
    print("NIE")


print("ZADANIE 6")
#Jeśli p jest liczbą pierwszą, to a^p - a mod p = 0
a = int(input("Liczba a: "))
p = int(input("Liczba p (jeśli pierwsza zwróci 'tak'): "))
if (a ** p - a) % p == 0 :
    print("TAK spełnia MTF")
else : 
    print("NIE spełnia MTF")


print("ZADANIE 7")
p = int(input("Początek: "))
k = int(input("Koniec: "))
s = int(input("Skok: "))
if s * 3 >= k - p:
    print("Żabka doskoczy")
else :
    print("Żabka nie doskoczy")