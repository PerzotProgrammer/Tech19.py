from random import randint

T = [randint(1, 1000) for i in range(10000)]


# JAKIŚ SPOSÓB Z INTERNETU

def QuickSort(T):
    if len(T) <= 1:
        return T
    else:
        pivot = T[0]
        Lewy = [x for x in T[1:] if x < pivot]
        Prawy = [x for x in T[1:] if x >= pivot]
    return QuickSort(Lewy) + [pivot] + QuickSort(Prawy)

T = QuickSort(T)
print(T)


T = [randint(1, 1000) for i in range(10000)]

# HOARE

def QuickSortHoare(T, lewy = 0, prawy = len(T) - 1):
    i = lewy
    j = prawy
    pivot = T[(lewy + prawy) // 2]

    while i <= j:
        while T[i] < pivot:
            i += 1
        while T[j] > pivot:
            j -= 1
        if i <= j:
            T[i], T[j] = T[j], T[i]
            i += 1
            j -= 1
    if lewy < j:
        QuickSortHoare(T, lewy, j)
    if prawy > i:
        QuickSortHoare(T, i, prawy)

QuickSortHoare(T)
print(T)

# LOMUTO

def QuickSortLomuto(T, lewy = 0, prawy = len(T) - 1):
    pivot = T[prawy]
    i = lewy
    for j in range(lewy, prawy):
        if T[j] <= pivot:
            T[i] , T[j] = T[j], T[i]
            i += 1
    T[i], T[prawy] = T[prawy], T[i]
    if lewy < i - 1:
        QuickSortLomuto(T, lewy, i - 1)
    if prawy > i + 1:
        QuickSortLomuto(T, i + 1, prawy)

QuickSortLomuto(T)
print(T)