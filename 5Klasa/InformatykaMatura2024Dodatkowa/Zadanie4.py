def wczytajPlik(sciezka: str) -> list[int]:
    arr = []
    with open(sciezka) as file:
        for line in file:
            arr.append(int(line.strip()))
    return arr


def zad42(sciezka: str):
    odbiorcy = wczytajPlik(sciezka)
    ileAdresatow = len(odbiorcy)
    ileOdbiorcow = len(set(odbiorcy))
    print(ileAdresatow - ileOdbiorcow)


def zad43(sciezka: str):
    odbiorcy = wczytajPlik(sciezka)
    minPakietu = 10000
    minTur = 10000

    for i in range(len(odbiorcy)):
        aktualnyKomputer = i
        pakiet = i + 1
        tury = 0

        while (aktualnyKomputer != i or tury == 0) and tury < len(odbiorcy):
            aktualnyKomputer = odbiorcy[aktualnyKomputer] - 1
            tury += 1

        if aktualnyKomputer == i:
            if tury < minTur or (tury == minTur and pakiet < minPakietu):
                minPakietu = pakiet
                minTur = tury

    print(f"{minTur} {minPakietu}")


def zad44(sciezka: str):
    odbiorcy = wczytajPlik(sciezka)
    pakiety = [1 for _ in range(len(odbiorcy))]

    for i in range(1, 9):
        nowePakiety = [0 for _ in range(len(odbiorcy))]
        for j in range(len(odbiorcy)):
            adresatIdx = odbiorcy[j]
            nowePakiety[adresatIdx - 1] += pakiety[j]
        pakiety = nowePakiety

        if i in [1, 2, 4, 8]:
            print(max(pakiety), end=" ")
    print()


if __name__ == '__main__':
    print("Zad 4.2 p")
    zad42("odbiorcy_przyklad.txt")
    print("Zad 4.2")
    zad42("odbiorcy.txt")
    print("Zad 4.3 p")
    zad43("odbiorcy_przyklad.txt")
    print("Zad 4.3")
    zad43("odbiorcy.txt")
    print("Zad 4.4 p")
    zad44("odbiorcy_przyklad.txt")
    print("Zad 4.4")
    zad44("odbiorcy.txt")
