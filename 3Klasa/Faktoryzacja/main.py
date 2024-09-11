import factorization as ft


def zad1():
    num = int(input("Podaj liczbę: "))
    pFact = ft.PrimeFactors(num)
    print(f"Czynniki pierwsze: {pFact}")


def zad2():
    num = int(input("Podaj liczbę: "))
    pFactSum = ft.SumOfFactors(num)
    print(f"Suma czynników pierwszych: {pFactSum}")


def zad3():
    num = int(input("Podaj liczbę: "))
    pFactSum = ft.SumOfFactors(num)
    if ft.IsPrime(pFactSum):
        print(f"Suma czynników pierwszych jest liczbą pierwszą")
    else:
        print(f"Suma czynników pierwszych nie jest liczbą pierwszą")


def zad4():
    num = int(input("Podaj liczbę: "))
    numOfDistFact = len(set(ft.PrimeFactors(num)))
    print(f"Liczba różnych czynników pierwszych: {numOfDistFact}")


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad4()
