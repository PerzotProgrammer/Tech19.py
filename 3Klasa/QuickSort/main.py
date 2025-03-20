from random import randint
from time import process_time

from QuickSort import *


def zad1():
    with open("./liczby.txt") as file:
        data = list(map(int, file.readlines()))

    output = QuickSort(data)
    print(output)


def zad2():
    with open("./liczby.txt") as file:
        data = list(map(int, file.readlines()))

    output = QuickSortPrint(data)
    print(output)


def zad3():
    with open("./liczby.txt") as file:
        data = list(map(int, file.readlines()))

    output = QuickSortV2(data)
    print(output)


def zad5():
    data = [randint(1, 1_000_000_000) for _ in range(1_000_000)]
    timeStart = process_time()
    QuickSort(data)
    timeEnd = process_time()
    print("QuickSort: took ", timeEnd - timeStart)
    timeStart = process_time()
    QuickSortV2(data)
    timeEnd = process_time()
    print("QuickSortV2: took ", timeEnd - timeStart)


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad5()
