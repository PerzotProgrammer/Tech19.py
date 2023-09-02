#zad1
print("ZADANIE 1")
a = int(input("Liczba1:"))
for i in range(0,a) : print((i*i*i)+3)

#zad2
print("ZADANIE 2")
for i in range(105,1000,+15) : print(i)

#zad3
print("ZADANIE 3")
a = int(input("Liczba1:"))
for i in range (0,a) : 
    if (a % i == 0) : print(i)

#zad4
print("ZADANIE 4")
a = 0
for i in range (10,100): a += i
print(a)

#zad5
print("ZADANIE 5")
a = int(input("Podaj ilość liczb: "))
b = a*(a+1)//2
for i in range (0,a-1) :
    x = int(input())
    b -= x
print("Nie napisałeś:",b)

#zad6
from time import sleep
print("ZADANIE 6")
x = 1
y = 1
while True:
    print(x)
    sleep(0.5)
    x+=y
    print(y)
    sleep(0.5)
    y+=x
