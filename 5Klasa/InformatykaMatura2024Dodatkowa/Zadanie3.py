def wczytajPlik(sciezka: str) -> list[str]:
    arr = []
    with open(sciezka) as file:
        for line in file:
            arr.append(line.strip())
    return arr


def zad31(sciezka: str):
    arr = wczytajPlik(sciezka)
    ile = 0
    for ciag in arr:
        for i in range(1, len(ciag) - 1):
            if ciag[i - 1] == 'k' and ciag[i + 1] == 't':
                ile += 1

    print(ile)


def cezar(ciag: str, n: int) -> str:
    poPrzesun = ""
    for litera in ciag:
        poPrzesun += chr((ord(litera) - ord('a') + n) % 26 + ord('a'))

    return poPrzesun


def zad32(sciezka: str):
    arr = wczytajPlik(sciezka)
    ile = 0
    for ciag in arr:
        if cezar(ciag, 13) == ciag[::-1]:
            ile += 1

    print(ile)


def zad33(sciezka: str):
    arr = wczytajPlik(sciezka)
    ile = 0
    for ciag in arr:
        wystLiter = {}
        for litera in ciag:
            if litera in wystLiter:
                wystLiter[litera] += 1
            else:
                wystLiter[litera] = 1
        for wartosci in wystLiter.items():
            if wartosci[1] >= len(ciag) / 2:
                ile += 1
                break

    print(ile)


if __name__ == '__main__':
    print("Zad 3.1 p")
    zad31("slowa_przyklad.txt")
    print("Zad 3.1")
    zad31("slowa.txt")
    print("Zad 3.2 p")
    zad32("slowa_przyklad.txt")
    print("Zad 3.2")
    zad32("slowa.txt")
    print("Zad 3.3 p")
    zad33("slowa_przyklad.txt")
    print("Zad 3.3")
    zad33("slowa.txt")
