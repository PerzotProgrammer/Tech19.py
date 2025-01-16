import SlidingWindow as sw


def zad1():
    with open("ciag.txt", "r") as file:
        T = list(map(int, file.read().split()))
    Subarrays = sw.GetAllSubarrays(T, 3)
    print(max([sum(subarray) for subarray in Subarrays]))


def zad2():
    with open("ciag.txt", "r") as file:
        T = list(map(int, file.read().split()))
    Subarrays = sw.GetAllSubarrays(T, 3)
    SumsOfArrays = [sum(subarray) for subarray in Subarrays]
    print(Subarrays[SumsOfArrays.index(max(SumsOfArrays))])


def zad3():
    with open("ciag.txt", "r") as file:
        T = list(map(int, file.read().split()))
    Subarrays = sw.GetAllSubarrays(T)
    print(max([sum(subarray) for subarray in Subarrays]))


def zad4():
    with open("ciag.txt", "r") as file:
        T = list(map(int, file.read().split()))
        maxSum = 0
        curSum = 0
    for i in T:
        curSum += i
        if i < 0:
            curSum = 0
        elif curSum > maxSum:
            maxSum = curSum
    print(maxSum)


def zad5():
    with open("ciag.txt", "r") as file:
        T = list(map(int, file.read().split()))
        start = 0
        i = 0
        maxSum = 0
        curSum = 0
    for i in range(len(T)):
        curSum += T[i]
        if T[i] < 0:
            curSum = 0
            start = i + 1
        elif curSum > maxSum:
            maxSum = curSum
    print(T[start:i + 1])


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
