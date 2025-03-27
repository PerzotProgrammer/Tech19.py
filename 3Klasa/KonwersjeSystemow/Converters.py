def IsBinary(binary: str) -> bool:
    binSet = set(binary)
    return binSet == {'0', '1', '.'} or binSet == {'1', '.'} or binSet == {'0', '1'} or binSet == {'1'}


def IsDecimal(decimal: str) -> bool:
    return decimal.isdigit()


def BinToDec(binary: str) -> float:
    parts = binary.split(".")
    binArr = list(map(int, parts[0]))[::-1]
    fracArr = list(map(int, parts[1]))
    decNum = 0
    for i in range(len(binArr)):
        decNum += binArr[i] * (2 ** i)

    for i in range(len(fracArr)):
        decNum += fracArr[i] * (2 ** (-i - 1))

    return decNum


def DecToBin(decimal: float) -> str:
    binNum = ""
    while decimal > 0:
        binNum += str(decimal % 2)
        decimal //= 2

    return binNum[::-1]
