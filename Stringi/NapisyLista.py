L = []
for i in range(1,10):
    L.append(i)

print(L)

# Zasada START:STOP:STEP

print(L[:4]) # Do czwartego elementu
print(L[::2]) # Co dwa
print(L[::-1]) # Od tyłu
print(L[6:]) # Od szóstego elementu

# ANAGRAMY
print("Anagram")

x = input("Daj input:")
y = input("Daj input:")

X = list(x)
Y = list(y)

X.sort()
Y.sort()

a = "".join(X)
b = "".join(Y)

if a == b: print(True)
else: print(False)

# Przez tablice
print("Anagram przez tablice")

x = input("Daj input:")
y = input("Daj input:")

# Tablice po 150 zer
X = [0] * 150
Y = [0] * 150

for i in range(len(x)):
    X[ord(x[i])] += 1
for i in range(len(y)):
    Y[ord(y[i])] += 1

if X == Y: print(True)
else: print(False)