def nieparzystySkrot(n: int) -> int:
    m = 0
    mnoznik = 1
    mnoznikReszty = 1

    while n > 0:
        reszta = (n % (mnoznik * 10)) // mnoznik
        if reszta % 2 != 0:
            m = m + (reszta * mnoznikReszty)
            mnoznikReszty = mnoznikReszty * 10
        n = n - (reszta * mnoznik)
        mnoznik = mnoznik * 10

    return m


def nwd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    return a


def zad3_2(plik: str):
    arr = []
    with open(plik) as file:
        for line in file:
            arr.append(int(line.strip()))

    ileBezSkrotu = 0
    najwieksza = 0

    for n in arr:
        if nieparzystySkrot(n) == 0:
            ileBezSkrotu = ileBezSkrotu + 1
            if n > najwieksza:
                najwieksza = n

    print(ileBezSkrotu)
    print(najwieksza)


def zad3_3(plik: str):
    arr = []
    with open(plik) as file:
        for line in file:
            arr.append(int(line.strip()))

    liczby = []

    for n in arr:
        skrot = nieparzystySkrot(n)
        if nwd(n, skrot) == 7:
            liczby.append(n)

    for n in liczby:
        print(n)


if __name__ == '__main__':
    print(nieparzystySkrot(294762))
    print(nieparzystySkrot(39101))
    print(nieparzystySkrot(224))

    print("zad 3.2 p")
    zad3_2("skrot_przyklad.txt")
    print("zad 3.2")
    zad3_2("skrot.txt")

    print("zad 3.3 p")
    zad3_3("skrot2_przyklad.txt")
    print("zad 3.3")
    zad3_3("skrot2.txt")
