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


def zad4():
    with open("liczby.txt") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))
        primes = soe.SieveOfEratostenes(max(numbers) + 1)
        count = 0
        for number in numbers:
            if primes[number]:
                count += 1
        print(f"W pliku jest {count} liczb pierwszych")
        file.close()


def zad5():
    num1 = int(input("Podaj 1 liczbę: "))
    num2 = int(input("Podaj 2 liczbę: "))
    low = min(num1, num2)
    high = max(num1, num2)
    primes = soe.SieveOfEratostenes(high + 1)
    numbers = []
    for i in range(low, high + 1):
        if primes[i]:
            numbers.append(i)
    print(f"Liczby pierwsze z przedziału <{low} ; {high}> - {numbers}, jest ich {len(numbers)} a ich suma to {sum(numbers)}")


if __name__ == '__main__':
    zad1()
    zad2()
    zad4()
    zad5()
