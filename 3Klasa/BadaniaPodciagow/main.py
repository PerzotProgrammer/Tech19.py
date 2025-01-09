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


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
