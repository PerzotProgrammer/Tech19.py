from random import randint
import BinarySearch as bs


def zad1oraz2(useRecursive=True):
    numbers = list(map(int, input("Podaj listę liczb: ").split()))
    if not bs.IsSorted(numbers):
        print("Lista musi być posortowana!")
        return
    searchedNumber = int(input("Podaj liczbę do znalezienia: "))

    if useRecursive:
        indexOfNumber = bs.BinarySearchRecursive(numbers, searchedNumber)
    else:
        indexOfNumber = bs.BinarySearch(numbers, searchedNumber)

    if indexOfNumber != -1:
        print(f"Liczba znajduje się w liście na indeksie {indexOfNumber}")
    else:
        print("Liczba nie znajduje się w liście")


def zad3():
    with open("ciagi.txt") as file:
        numberLists = []
        for line in file:
            numberLists.append(list(map(int, line.split())))
        for numberList in numberLists:
            if bs.BinarySearch(numberList, 10) != -1:
                print(numberList)
        file.close()


def zad4():
    with open("ciagi2.txt") as file:
        numberLists = []
        dataLatch = True
        for line in file:
            if dataLatch:
                numberLists.append(list(map(int, line.split())))
            dataLatch = not dataLatch
        numberLists.pop(0)
        for numberList in numberLists:
            if bs.BinarySearch(numberList, 10) != -1:
                print(numberList)
        file.close()


def zad6():
    numbers = [randint(1, 10)]
    for i in range(1, 1_000_000):
        numbers.append(numbers[i - 1] + randint(1, 3))
    comps = bs.BinarySearch(numbers, 1_500_000, True)
    with open("zad6.txt", "w") as file:
        if comps > -1:
            file.write(f"Tak\n{comps}")
        else:
            file.write(f"Nie\n{comps * -1}")
        file.close()


if __name__ == "__main__":
    # zad1oraz2()
    # zad3()
    # zad4()
    zad6()
