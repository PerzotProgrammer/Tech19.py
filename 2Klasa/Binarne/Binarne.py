def IsEvenBin(numBin: int) -> bool:
    numBinDec = int(numBin)
    return numBinDec % 2 == 0


def IsEvenSumBin(numBinA: int, numBinB: int) -> bool:
    return IsEvenBin(numBinA) == IsEvenBin(numBinB)


def IsEvenProductBin(numBinA: int, numBinB: int) -> bool:
    return IsEvenBin(numBinA) or IsEvenBin(numBinB)


def AddBin(numBinA: int, numBinB: int) -> str:
    return bin(numBinA + numBinB)


def AddBinStr(numBinA: int, numBinB: int) -> str:
    numBinAStr = str(numBinA)
    numBinBStr = str(numBinB)
    output = ""
    div = 0

    for i in range(len(numBinAStr) - 1, -1, -1):
        checkSum = div + int(numBinAStr[i]) + int(numBinBStr[i])
        div = checkSum // 2
        output = str(checkSum % 2) + output
    if div > 0:
        output = str(div) + output
    return output
