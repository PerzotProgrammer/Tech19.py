from random import randint

from MinMax import *


def zad1():
    Arr = [randint(1, 1000) for _ in range(100)]
    print(Arr)
    print(MinMaxNaive(Arr))


def zad3():
    Arr = [randint(1, 1000) for _ in range(100)]
    print(Arr)
    print(MinMax(Arr))


if __name__ == "__main__":
    zad1()
    zad3()
