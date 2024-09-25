def SieveOfEratostenes(lengthOfList: int) -> []:
    boolList = [True for _ in range(0, lengthOfList)]
    boolList[0] = False
    boolList[1] = False
    div = 2
    while div * div <= lengthOfList:
        if boolList[div]:
            for i in range(div * div, lengthOfList, div):
                boolList[i] = False
        div += 1
    return boolList
