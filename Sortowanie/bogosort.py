from random import randint

T = [randint(1, 1000) for i in range(10)]
reku = 0
# BŁAGAM NIE UŻYWAJCIE TEGO

def BogoSort(T : list, reku):
    while CzyPosortowana(T) == False:
        Randomuj(T)
        reku += 1
    return reku


def CzyPosortowana(T):
    for i in range(1, len(T)):
        if T[i - 1] >= T[i]:
            return False
    return True

def Randomuj(T):
    for i in range(len(T)):
        random = randint(0, len(T) - 1)
        T[i], T[random] = T[random], T[i]

# Zmienna reku jest po to aby liczyć ilość rekurencji
reku = BogoSort(T, reku)
print(T,"Rekurencje:", reku)