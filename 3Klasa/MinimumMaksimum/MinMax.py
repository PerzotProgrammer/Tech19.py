def MinMaxNaive(Array: list[int]) -> tuple[int, int]:
    minValue = Array[0]
    maxValue = Array[0]
    for i in range(1, len(Array)):
        if Array[i] < minValue:
            minValue = Array[i]
        if Array[i] > maxValue:
            maxValue = Array[i]

    return minValue, maxValue


def MinMax(Array: list[int]) -> tuple[int, int]:
    minValue, maxValue = CompareAndReplace(Array[0], Array[1])
    for i in range(2, len(Array) - 1, 2):
        minValueTemp, maxValueTemp = CompareAndReplace(Array[i], Array[i + 1])
        if minValueTemp < minValue:
            minValue = minValueTemp
        if maxValueTemp > maxValue:
            maxValue = maxValueTemp
    return minValue, maxValue


def CompareAndReplace(a: int, b: int) -> tuple[int, int]:
    if a < b:
        return a, b
    return b, a
