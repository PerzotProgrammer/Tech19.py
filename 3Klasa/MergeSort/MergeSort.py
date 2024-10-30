def Sort(T: [int], left=0, right=None) -> [int]:
    if right is None:
        right = len(T) - 1
    Temp = [0 for _ in range(len(T))]
    if left < right:
        middle = (left + right) // 2
        Sort(T, left, middle)
        Sort(T, middle + 1, right)
        Merge(T, left, middle, right, Temp)
    return T


def Merge(T: [int], left: int, middle: int, right: int, Temp: [int]) -> None:
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
