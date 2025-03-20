def QuickSort(arr, left=0, right=None) -> list[int]:
    if right is None:
        right = len(arr) - 1
    lCopy = left
    rCopy = right
    mid = (left + right) // 2
    while left <= right:
        while arr[left] < arr[mid]:
            left += 1
        while arr[right] > arr[mid]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    if right > lCopy:
        return QuickSort(arr, lCopy, right)
    if left < rCopy:
        return QuickSort(arr, left, rCopy)
    return arr


def QuickSortPrint(arr, left=0, right=None) -> list[int]:
    if right is None:
        right = len(arr) - 1
    lCopy = left
    rCopy = right
    mid = (left + right) // 2
    print(arr[lCopy:rCopy])
    while left <= right:
        while arr[left] < arr[mid]:
            left += 1
        while arr[right] > arr[mid]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    if right > lCopy:
        return QuickSortPrint(arr, lCopy, right)
    if left < rCopy:
        return QuickSortPrint(arr, left, rCopy)
    return arr


def QuickSortV2(arr) -> list[int]:
    n = len(arr)
    if n < 2:
        return arr
    mid = arr[n // 2]
    left = []
    middle = []
    right = []
    for elem in arr:
        if elem < mid:
            left.append(elem)
        if elem == mid:
            middle.append(elem)
        if elem > mid:
            right.append(elem)
    return QuickSortV2(left) + middle + QuickSortV2(right)
