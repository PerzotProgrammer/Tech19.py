def MergeSort(T: [int]) -> [int]:
    Temp = [0 for _ in range(len(T))]
    return Sort(T, Temp, 0, len(T) - 1)


def Sort(T: [int], Temp: [int], left: int, right: int) -> [int]:
    if left < right:
        middle = (left + right) // 2
        Sort(T, Temp, left, middle)
        Sort(T, Temp, middle + 1, right)
        Merge(T, Temp, left, middle, right)
    return T


def Merge(T: [int], Temp: [int], left: int, middle: int, right: int) -> None:
    i = left
    j = middle + 1
    k = left
    while i <= middle and j <= right:
        if T[i] < T[j]:
            Temp[k] = T[i]
            i += 1
        else:
            Temp[k] = T[j]
            j += 1
        k += 1
    while i <= middle:
        Temp[k] = T[i]
        i += 1
        k += 1
    while j <= right:
        Temp[k] = T[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        T[i] = Temp[i]
