import skryptyPowtorka as sp


def zad1():
    num = int(input('Podaj liczbę: '))
    if sp.IsEven(num):
        print("Jest parzysta")
    else:
        print("Nie jest parzysta")


def zad2():
    num = int(input('Podaj liczbę: '))
    divs = sp.Dividers(num)
    print(f'Dzielniki: {divs}')


def zad3():
    num = int(input('Podaj liczbę: '))
    divs = sum(sp.Dividers(num))
    print(f'Suma dzielników: {divs}')


def zad4():
    num = int(input('Podaj liczbę: '))
    divs = len(sp.Dividers(num))
    print(f'Liczba dzielników: {divs}')


def zad5():
    num = int(input('Podaj liczbę: '))
    divs = sp.PrimeDividers(num)
    print(f"Dzielniki pierwsze: {divs}")


def zad6():
    num1 = int(input('Podaj 1 liczbę: '))
    num2 = int(input('Podaj 2 liczbę: '))
    if sp.AreNumbersTwins(num1, num2):
        print("Liczby są bliźniacze")
    else:
        print("Liczby nie są bliźniacze")


def zad7():
    num = int(input('Podaj liczbę: '))
    if sp.IsPerfectNumber(num):
        print("Jest to liczba doskonała")
    else:
        print("Nie jest to liczba doskonała")


if __name__ == '__main__':
    print("zad1")
    zad1()
    print("zad2")
    zad2()
    print("zad3")
    zad3()
    print("zad4")
    zad4()
    print("zad5")
    zad5()
    print("zad6")
    zad6()
    print("zad7")
    zad7()
