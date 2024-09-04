def IsEven(num: int) -> bool:
    return num % 2 == 0


def Dividers(num: int) -> []:
    dividers = []
    for i in range(2, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers
