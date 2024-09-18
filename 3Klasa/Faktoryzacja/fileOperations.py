from factorization import IsPrime, PrimeFactors


def Dividers(num: int) -> []:
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers


def ProperDividers(num: int) -> []:
    dividers: list = Dividers(num)
    dividers.remove(num)
    return dividers


def PrimeDividers(num: int) -> []:
    dividers: [] = Dividers(num)
    primeDividers = []
    for divider in dividers:
        if IsPrime(divider):
            primeDividers.append(divider)
    return primeDividers


def Ex1():
    with open("Numbers/liczby1.txt", "r") as f:
        lines = f.readlines()
        primes = []
        for line in lines:
            if IsPrime(int(line)):
                primes.append(int(line))
        print(f"W pliku jest {len(primes)} liczb pierwszych")
    f.close()


def Ex2():
    with open("Numbers/liczby2.txt", "r") as f:
        nums = f.readline().split(" ")
        for num in nums:
            if int(num) % 2 == 0:
                print(num)
    f.close()


def Ex3():
    with open("Numbers/liczby2.txt", "r") as f:
        nums = f.readline().split(" ")
        numOfDividers = 0
        for num in nums:
            numOfDividers += len(ProperDividers(int(num)))
    print(f"Ilość dzielników właściwych: {numOfDividers}")
    f.close()


def Ex4():
    with open("Numbers/liczby2.txt", "r") as f:
        nums = f.readline().split(" ")
        bestNum = 0
        bestDivSum = 0
        for num in nums:
            if sum(PrimeDividers(int(num))) > bestDivSum:
                bestDivSum = sum(PrimeDividers(int(num)))
                bestNum = int(num)
    print(f"Liczba z największą sumą dzielników pierwszych: {bestNum}")
    f.close()


def Ex5():
    with open("Numbers/liczby2.txt", "r") as f:
        nums = f.readline().split(" ")
        output = []
        lowestPrimeFactorSum = sum(PrimeFactors(int(nums[0])))
        for num in nums:
            if sum(PrimeFactors(int(num))) == lowestPrimeFactorSum:
                output.append(int(num))
            elif sum(PrimeFactors(int(num))) < lowestPrimeFactorSum:
                output.clear()
                lowestPrimeFactorSum = sum(PrimeFactors(int(num)))
    print(f"Liczby z najmniejszą sumą czynników pierwszych: {output}")
    f.close()


def Ex6():
    with open("Numbers/liczby2.txt", "r") as f:
        nums = f.readline().split(" ")
        output = []
        for num in nums:
            pFactors = list(set(PrimeFactors(int(num))))
            lastFactor = pFactors[0]
            if len(pFactors) < 2:
                continue
            for pFactor in pFactors:
                if pFactor != lastFactor:
                    continue
            output.append(int(num))
    print(f"Liczby, które mają przynajmniej dwa różne czynniki pierwsze: {output}")
    f.close()


def Exercises():
    Ex1()
    Ex2()
    Ex3()
    Ex4()
    Ex5()
    Ex6()
