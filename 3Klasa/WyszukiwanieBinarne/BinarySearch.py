def BinarySearch(numbers: list, target: int) -> int:
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def BinarySearchRecursive(numbers: list, target: int, low=-1, high=-1) -> int:
    if low == -1 or high == -1:
        low = 0
        high = len(numbers) - 1
    mid = (low + high) // 2
    if numbers[mid] == target:
        return mid
    elif low >= high:
        return -1
    if numbers[mid] < target:
        return BinarySearchRecursive(numbers, target, mid + 1, high)
    elif numbers[mid] > target:
        return BinarySearchRecursive(numbers, target, low, mid - 1)


def IsSorted(numbers: list) -> bool:
    for i in range(len(numbers)):
        if numbers[i] > numbers[i + 1]:
            return False
    return True
