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
