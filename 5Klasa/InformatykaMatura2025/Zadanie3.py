from operator import and_


def zwroc_plik(sciezka: str) -> list[str]:
    arr = []

    with open(sciezka) as file:
        for line in file:
            arr.append(line.strip())
    return arr


def nwd(a: int, b: int) -> int:
    if b == 0:
        return a
    a = abs(a)
    b = abs(b)

    while b > 0:
        a, b = b, a % b

    return a


def zad3_1(sciezka: str):
    arr = zwroc_plik(sciezka)
    ile_nwd = 0

    for ciag in arr:
        liczby = list(map(int, ciag.split(" ")))
        if nwd(liczby[0], liczby[1]) > 1:
            ile_nwd += 1

    print(ile_nwd)


def zad3_2(sciezka: str):
    arr = zwroc_plik(sciezka)
    ile_wierzcholkow = 0

    pos_x = 0
    pos_y = 0
    punkty = []

    for i in range(len(arr)):
        dx, dy = list(map(int, arr[i].split(" ")))
        pos_x += dx
        pos_y += dy
        punkty.append([pos_x, pos_y])

        if 0 < pos_x < 5000 and 0 < pos_y < 5000:
            ile_wierzcholkow += 1

    print(f"a) {ile_wierzcholkow}")

    for i in range(len(punkty)):
        for j in range(i + 1, len(punkty)):
            for k in range(j + 1, len(punkty)):
                A = punkty[i]
                B = punkty[j]
                C = punkty[k]

                if A[0] + C[0] == 2 * B[0] and A[1] + C[1] == 2 * B[1]:
                    print("b)", A, B, C)

                elif A[0] + B[0] == 2 * C[0] and A[1] + B[1] == 2 * C[1]:
                    print("b)", A, B, C)

                elif B[0] + C[0] == 2 * A[0] and B[1] + C[1] == 2 * A[1]:
                    print("b)", A, B, C)


if __name__ == '__main__':
    print("Zadanie 3.1 p")
    zad3_1("dron_przyklad.txt")

    print("Zadanie 3.1")
    zad3_1("dron.txt")

    print("Zadanie 3.2 p")
    zad3_2("dron_przyklad.txt")

    print("Zadanie 3.2")
    zad3_2("dron.txt")
