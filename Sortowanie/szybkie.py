from random import randint

T = [randint(1, 1000) for i in range(10000)]


def QuickSort(T):
    if len(T) <= 1:
        return T
    else:
        pivot = T[0]
        # Chciałem w forach ale nie działało
        Lewy = [x for x in T[1:] if x < pivot]
        Prawy = [x for x in T[1:] if x >= pivot]
    return QuickSort(Lewy) + [pivot] + QuickSort(Prawy)

T = QuickSort(T)
print(T)

