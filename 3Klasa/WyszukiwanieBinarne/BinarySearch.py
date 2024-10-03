def BinarySearch(numbers: list, target: int, numOfCompMode=False) -> int:
    low = 0
    high = len(numbers) - 1
    numOfComps = 0
    while low <= high:
        mid = (low + high) // 2
        numOfComps += 1
        if numbers[mid] == target:
            if numOfCompMode:
                return numOfComps
            return mid
        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if numOfCompMode:
        return -numOfComps
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
    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            return False
    return True
