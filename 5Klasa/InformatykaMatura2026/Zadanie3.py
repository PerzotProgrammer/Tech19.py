def wczytajPary(sciezka: str) -> list[tuple[str, str]]:
    arr = []
    with open(sciezka) as file:
        for line in file:
            arr.append(tuple(map(str, line.strip().split(" "))))
    return arr


def sumaKodowAscii(ciag: str) -> int:
    suma = 0
    for znak in ciag:
        suma += ord(znak)
    return suma


def zad31(sciezka: str):
    arr = wczytajPary(sciezka)
    najwiekszaSuma = 0
    najwiekszaPara = ()
    for para in arr:
        wBezwzglednaRoznicySumy = abs(sumaKodowAscii(para[0]) - sumaKodowAscii(para[1]))
        if wBezwzglednaRoznicySumy > najwiekszaSuma:
            najwiekszaPara = para
            najwiekszaSuma = wBezwzglednaRoznicySumy

    print(f"{najwiekszaPara[0]} {najwiekszaPara[1]} {najwiekszaSuma}")


def d(x: str, s: str) -> int:
    ile = 0
    for c in s:
        if c == x:
            ile += 1
    return ile


def W(x: str, s1: str, s2: str) -> int:
    return min(d(x, s1), d(x, s2))


def zad32(sciezka: str):
    arr = wczytajPary(sciezka)

    najwiekszaSuma = 0
    najwiekszaPara = ()

    for para in arr:
        wspolneLitery = list(set(list(para[0])).intersection(set(list(para[1]))))
        suma = 0
        for litera in wspolneLitery:
            suma += W(litera, para[0], para[1])
        if suma > najwiekszaSuma:
            najwiekszaSuma = suma
            najwiekszaPara = para

    print(f"{najwiekszaPara[0]} {najwiekszaPara[1]} {najwiekszaSuma}")


def wspolnyPrefiksosufiks(s1: str, s2: str) -> str:
    wspolne = ""
    for i in range(min(len(s1), len(s2))):
        if s2.endswith(s1[:i]):
            wspolne = s1[:i]
    return wspolne


def zad33(sciezka: str):
    arr = wczytajPary(sciezka)

    for para in arr:
        dlugosc = max(len(wspolnyPrefiksosufiks(para[0], para[1])), len(wspolnyPrefiksosufiks(para[1], para[0])))

        if dlugosc >= 5:
            print(f"{para} {dlugosc}")


if __name__ == '__main__':
    print("Zadanie 3.1 p")
    zad31("pary_przyklad.txt")
    print("Zadanie 3.1")
    zad31("pary.txt")
    print("Zadanie 3.2 p")
    zad32("pary_przyklad.txt")
    print("Zadanie 3.2")
    zad32("pary.txt")
    print("Zadanie 3.3 p")
    zad33("pary_przyklad.txt")
    print("Zadanie 3.3")
    zad33("pary.txt")
