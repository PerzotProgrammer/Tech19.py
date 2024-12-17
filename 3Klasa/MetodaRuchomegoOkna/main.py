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


def mat1():
    with open("pi.txt") as file:
        pi = file.read().replace("\n", "")
        sumOfNums = 0
        for i in range(len(pi) - 1):
            num = int(pi[i] + pi[i + 1])
            if num > 90:
                sumOfNums += 1
    print(sumOfNums)


def mat2():
    freq = [0 for _ in range(100)]
    with open("pi.txt") as file:
        pi = file.read().replace("\n", "")
        for i in range(len(pi) - 1):
            num = int(pi[i] + pi[i + 1])
            freq[num] += 1
        print(f"{freq.index(min(freq))} {min(freq)}")
        print(f"{freq.index(max(freq))} {max(freq)}")


def mat3():
    with open("pi.txt") as file:
        pi = file.read().replace("\n", "")
        low = 0
        high = 6
        count = 0
        while high < len(pi):
            flagUp = True
            flagDown = False
            for i in range(low + 1, high):
                if flagUp and pi[i - 1] <= pi[i]:
                    flagDown = True
                elif flagDown and pi[i - 1] >= pi[i]:
                    flagDown = True
                    flagUp = False
                else:
                    flagUp = False
                    flagDown = False
                    break
            if not flagUp and flagDown:
                count += 1
            low += 1
            high += 1
        print(count)


if __name__ == '__main__':
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    mat1()
    mat2()
    mat3()
