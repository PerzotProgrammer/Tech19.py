def BinConvertBasic(decNum: int) -> int:
    return int(bin(decNum)[2:])


def BinConvertMath(decNum: int) -> int:
    output = ""
    while decNum > 0:
        output = str(decNum % 2) + output
        decNum //= 2
    return int(output)


def BinConvertRecursive(decNum: int) -> int:
    if decNum == 0:
        return 0
    else:
        return decNum % 2 + 10 * BinConvertRecursive((decNum // 2))
