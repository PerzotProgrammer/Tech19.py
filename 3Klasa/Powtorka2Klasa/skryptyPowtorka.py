def IsEven(num: int) -> bool:
    return num % 2 == 0


def Dividers(num: int) -> []:
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers


def IsPrime(num: int) -> bool:
    if num <= 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def PrimeDividers(num: int) -> []:
    dividers: [] = Dividers(num)
    primeDividers = []
    for divider in dividers:
        if IsPrime(divider):
            primeDividers.append(divider)
    return primeDividers


def AreNumbersTwins(a: int, b: int) -> bool:
    if IsPrime(a) and IsPrime(b) and abs(a - b) == 2:
        return True
    return False


def IsPerfectNumber(num: int) -> bool:
    dividers: [] = Dividers(num)
    dividers.remove(num)
    if sum(dividers) == num:
        return True
    return False
