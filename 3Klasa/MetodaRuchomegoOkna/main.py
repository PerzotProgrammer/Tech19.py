import SlidingWindow as sw


def zad1():
    sw.PrintAllSubarraysEx1(list(map(int, input("Podaj ciąg: ").split())))


def zad2():
    sw.PrintAllSubarraysEx2(list(map(int, input("Podaj ciąg: ").split())))


def zad3():
    with open("liczby.txt") as file:
        numbers = list(map(int, file.read().split()))
        subarrays = sw.GetAllSubarrays(numbers)
        for subarray in subarrays:
            if len(subarray) == 5:
                print(f"{subarray} suma elementów: {sum(subarray)}")


def zad4():
    with open("liczby.txt") as file:
        numbers = list(map(int, file.read().split()))
        subarrays = sw.GetAllSubarrays(numbers)
        for subarray in subarrays:
            if len(subarray) > 3:
                print(subarray)


def zad5():
    numbers = list(map(int, input("Podaj ciąg: ").split()))
    lastNum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] <= lastNum:
            print("Ciąg nie jest rosnący")
            return
        lastNum = numbers[i]
    print("Ciąg jest rosnący")


def zad6():
    numbers = list(map(int, input("Podaj ciąg: ").split()))
    lastNum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] >= lastNum:
            print("Ciąg nie jest malejący")
            return
        lastNum = numbers[i]
    print("Ciąg jest malejący")


if __name__ == '__main__':
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    zad5()
    zad6()
