import SieveOfEratosthenes as soe


def zad1():
    num = int(input("Podaj liczbę: ")) + 1
    primes = soe.SieveOfEratostenes(num)
    for i in range(num):
        if primes[i]:
            print(i)


def zad2():
    num = int(input("Podaj liczbę: ")) + 1
    primes = soe.SieveOfEratostenes(num)
    sumOfPrimes = 0
    numOfPrimes = 0
    for i in range(num):
        if primes[i]:
            sumOfPrimes += i
            numOfPrimes += 1
    print(f"Jest {numOfPrimes} liczb pierwszych a ich suma to {sumOfPrimes}")


if __name__ == '__main__':
    zad1()
    zad2()