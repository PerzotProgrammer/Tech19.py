def PrimeFactors(n: int) -> []:
    primeFactors = []
    div = 2
    while n > 1:
        while n % div == 0:
            primeFactors.append(div)
            n //= div
        div += 1
    return primeFactors


def SumOfFactors(n: int) -> int:
    sumOfFactors = 0
    primeFactors = PrimeFactors(n)
    for prime in primeFactors:
        sumOfFactors += prime
    return sumOfFactors


def IsPrime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def SumOfDigits(n: int) -> int:
    sumOfDigits = 0
    for i in str(n):
        sumOfDigits += int(i)
    return sumOfDigits


def IsSmithNumber(n: int) -> bool:
    pFactors = PrimeFactors(n)
    sumOfDigitsInFactors = 0
    for i in pFactors:
        sumOfDigitsInFactors += SumOfDigits(i)
    if sumOfDigitsInFactors == SumOfDigits(n):
        return True
    return False


def Exercises():
    num = int(input("Podaj liczbę: "))
    pFact = PrimeFactors(num)
    print(f"Czynniki pierwsze: {pFact}")
    pFactSum = SumOfFactors(num)
    print(f"Suma czynników pierwszych: {pFactSum}")
    if IsPrime(pFactSum):
        print(f"Suma czynników pierwszych jest liczbą pierwszą")
    else:
        print(f"Suma czynników pierwszych nie jest liczbą pierwszą")
    numOfDistFact = len(set(PrimeFactors(num)))
    print(f"Liczba różnych czynników pierwszych: {numOfDistFact}")
    if IsSmithNumber(num):
        print(f"Liczba jest liczbą Smitha")
    else:
        print(f"Liczna nie jest liczbą Smitha")
