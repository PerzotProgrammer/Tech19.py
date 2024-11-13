def Naive(x: int, a: list) -> int:
    result = a[0]
    power = 1
    for i in range(1, len(a)):
        power = power * x
        result += a[i] * power
    return result


def Horner(x: int, a: list) -> int:
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result


def HornerRecursive(x: int, a: list) -> int:
    if len(a) == 1:
        return a[0]
    return x * HornerRecursive(x, a[1:]) + a[0]
