import Horner


def zad1():
    a = list(map(int, input("Podaj wielomiany: ").split()))
    x = int(input("Podaj x: "))
    print(f"Twój Naiwny: {Horner.Naive(x, a)}")


def zad2():
    a = list(map(int, input("Podaj wielomiany: ").split()))
    x = int(input("Podaj x: "))
    print(f"Twój Horner: {Horner.Horner(x, a)}")


def zad3():
    a = list(map(int, input("Podaj wielomiany: ").split()))
    x = int(input("Podaj x: "))
    print(f"Twój Horner Rekurencyjny: {Horner.HornerRecursive(x, a)}")


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()