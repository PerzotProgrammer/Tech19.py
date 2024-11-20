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


def zad6():
    a = list(map(int, input("Podaj liczbę binarną: ")))
    print(f"Twoja liczba binarna w formie decymalnej: {Horner.Horner(2, a)}")


def zad7():
    a = list(map(int, input("Podaj liczbę w wybranym systemie: ")))
    x = int(input("Podaj podstawę systemu: "))
    print(f"Twoja liczba systemu o podstawie {x} w formie decymalnej: {Horner.Horner(x, a)}")


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad6()
    zad7()
