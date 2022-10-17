# POST - utrwalenie pętli

# Pętle for liczb trzycyforowych podzielnych przez 13 (2 sposoby)

# Pętle for liczb dwucyfrowych parzystych (3 sposoby)
    
# Pętle for potęg cyfr: WY: 0, 1, 4, 9, 16 .. 81 (2 sposoby printa)

#zad1
print("ZADANIE 1.1")
for i in range(100,1000):
    if i % 13 == 0:
        print(i)

print("ZADANIE 1.2")
for i in range(104,1000,+13):
    print(i)

#zad2
print("ZADANIE 2.1")
for i in range(10,100):
    if i % 2 == 0:
        print(i)

print("ZADANIE 2.2")
for i in range(10,100,+2):
    print(i)

print("ZADANIE 2.3")
for i in range(5,50):
    print(i*2)

#zad3
print("ZADANIE 3.1")
for i in range(1,100):
    print(i*i)

print("ZADANIE 3.2")
for i in range(1,100):
    print(pow(i,2))