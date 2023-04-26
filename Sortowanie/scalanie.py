from random import randint

T = [randint(1, 1000) for i in range(10000)]

# TODO WORK IN PROGRESS

def Scalaj(lewo, prawo):
    L = T.copy()
    srodek = (lewo + prawo) // 2
    i = lewo
    iLewy = lewo
    iPrawy = srodek
    while(iLewy <= srodek and iPrawy < prawo):
        if L[iLewy] < L[iPrawy]:
            L[i] = T[iLewy]
            iLewy += 1
        else:
            T[i] = L[iPrawy]
            iPrawy += 1
        i += 1



def Sortuj(lewo, prawo):
    srodek = (lewo + prawo) // 2
    if lewo < srodek:
        Sortuj(lewo, srodek)
        if srodek + 1 < prawo: pass


print(T)