# FOREACH
# foreach x in L == for x in range(len(L))

L = [1,2,3,5,8,13]

def foreach(L):
    for i in range(len(L)):
        print(L[i],end=", ")
    print()

print("Lista L:",end=" ")
foreach(L)

# METODY DO LIST
# append()    dodaje do listy
# clear()     czyści listę
# extend()    łączy listy
# index()     daje indeks danej wartości
# count()     usuwa dany indeks
# insert()    dodaje element na dany indeks
# remove()    usuwa z listy pierwszy element z listy o podanej wartości
# reverse()   odwraca listę

print("Dalej lista K: ")
K = [3,5,6,2,11,23,67,3,3,92538,6374,153264,153]

print(f"K zwykłe:\n{K}")
K.append(134)
print(f"K.append(134):\n{K}")
print(f"K.index(23):\n{K.index(23)}")
print(f"K.count(3):\n{K.count(3)}")

