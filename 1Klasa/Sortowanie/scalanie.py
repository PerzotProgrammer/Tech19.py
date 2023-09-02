from random import randint

T = [randint(1, 1000) for i in range(10000)]


def Scalaj(lewo, prawo):
    Tkopia = T.copy()
    srodek = (lewo + prawo) // 2
    i = lewo
    iLewo = lewo
    iPrawo = srodek + 1

    while iLewo <= srodek and iPrawo <= prawo:
        if Tkopia[iLewo] < Tkopia[iPrawo]:
            T[i] = Tkopia[iLewo]
            iLewo += 1
        else:
            T[i] = Tkopia[iPrawo]
            iPrawo += 1
        i += 1
    if iLewo > srodek:
        while iPrawo <= prawo:
            T[i] = Tkopia[iPrawo]
            iPrawo += 1
            i += 1
    else:
        while iLewo <= srodek:
            T[i] = Tkopia[iLewo]
            iLewo += 1
            i += 1

def MergeSort(lewo = 0, prawo = len(T) - 1):
    srodek = (lewo + prawo) // 2
    if lewo < srodek:
        MergeSort(lewo, srodek)
    if srodek + 1 < prawo:
        MergeSort(srodek + 1, prawo)
    Scalaj(lewo, prawo)

MergeSort()
print(T)