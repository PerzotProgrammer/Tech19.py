from Converters import *


def zad6():
    print("Podaj liczbę binarną: ", end="")
    num = input()
    if IsBinary(num):
        print(f"Twoja liczba dziesiętna: {BinToDec(num)}")
    else:
        print("Podana liczba nie jest binarna")


def zad7():
    print("Podaj liczbę dziesiętną: ", end="")
    num = input()
    if IsDecimal(num):
        print(f"Twoja liczba binarna: {DecToBin(int(num))}")
    else:
        print("Podana liczba nie jest dziesiętna")


if __name__ == "__main__":
    zad6()
    zad7()