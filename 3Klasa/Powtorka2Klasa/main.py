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


if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
